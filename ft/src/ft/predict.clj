(ns ft.predict
  "Detrend + Fourier model, with reconstruction and extrapolation."
  (:require [ft.fft :as fft]))

(defn linfit
  "Least-squares fit of y = a + b*x over x = 0..n-1. Returns {:a :b}."
  [ys]
  (let [n (count ys)
        xs (range n)
        sx (double (reduce + xs))
        sy (double (reduce + ys))
        sxx (double (reduce + (map #(* (double %) (double %)) xs)))
        sxy (double (reduce + (map #(* (double %) (double %2)) xs ys)))
        denom (- (* n sxx) (* sx sx))
        b (if (zero? denom) 0.0 (/ (- (* n sxy) (* sx sy)) denom))
        a (/ (- sy (* b sx)) n)]
    {:a a :b b}))

(defn detrend
  "Remove the fitted straight line from the window."
  [ys]
  (let [{:keys [a b]} (linfit ys)]
    (mapv (fn [i y] (- (double y) (+ a (* b i)))) (range (count ys)) ys)))

(defn fit
  "Fit a Fourier model to a window of prices.
   Keeps the `k` strongest frequency components.
   Returns {:a :b :n :spectrum :bins}."
  [ys k]
  (let [{:keys [a b]} (linfit ys)
        spectrum (fft/forward (detrend ys))]
    {:a a :b b :n (count ys) :k k :spectrum spectrum
     :bins (fft/top-bins spectrum k)}))

(defn- bin-term
  "Real contribution of positive-frequency bin k at index t
   (includes the conjugate bin's contribution): (2/n)·Re(X[k]·e^{iθ})."
  [spectrum n k t]
  (let [[re im] (nth spectrum k)
        theta (/ (* 2.0 Math/PI k t) n)]
    (* (/ 2.0 n) (- (* re (Math/cos theta)) (* im (Math/sin theta))))))

(defn predict-at
  "Predict the price at integer index `t`. t may exceed the fit window,
   which extrapolates the fitted trend and sinusoids forward.

   Sums DC + selected positive-frequency bins + the Nyquist bin, i.e. the
   real-signal inverse transform. When every positive bin is selected this
   reproduces the fitted window exactly."
  [model t]
  (let [{:keys [a b n spectrum bins]} model
        [re0 _] (nth spectrum 0)
        dc (/ (double re0) n)
        nyq (if (even? n)
              (let [[ren _] (nth spectrum (quot n 2))]
                (* (/ (double ren) n) (if (even? t) 1.0 -1.0)))
              0.0)
        sinus (reduce + 0.0 (map (fn [{:keys [k]}] (bin-term spectrum n k t)) bins))]
    (+ a (* b t) dc nyq sinus)))

(defn predict-series
  "Predict `count` points starting at index `start`."
  [model start count]
  (mapv #(predict-at model %) (range start (+ start count))))
