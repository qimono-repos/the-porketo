(ns ft.predict-test
  (:require [clojure.test :refer [deftest is testing]]
            [ft.predict :as predict]))

(deftest linfit-recovers-a-line
  (let [{:keys [a b]} (predict/linfit (mapv #(+ 3.0 (* 2.0 %)) (range 10)))]
    (is (< (Math/abs (- a 3.0)) 1e-9))
    (is (< (Math/abs (- b 2.0)) 1e-9))))

(deftest detrend-removes-the-line
  (let [ys (mapv #(+ 3.0 (* 2.0 %)) (range 10))
        det (predict/detrend ys)]
    (is (every? #(< (Math/abs (double %)) 1e-9) det))))

(defn- trend-signal [n a b amp f phase]
  (mapv (fn [i] (+ a (* b i) (* amp (Math/sin (+ (/ (* 2.0 Math/PI f i) n) phase)))))
        (range n)))

(defn- periodic-at
  "Value at index t of a cosine sum that is even about the window centre."
  [n a spec c t]
  (+ a (reduce + 0.0 (map (fn [[f amp]]
                            (* amp (Math/cos (/ (* 2.0 Math/PI f (- t c)) n))))
                          spec))))

(deftest fit-identifies-the-dominant-frequency
  (let [model (predict/fit (trend-signal 64 100.0 0.25 7.0 5 0.6) 3)]
    (is (= 5 (:k (first (:bins model)))))))

(deftest full-bin-model-reconstructs-window-exactly
  (let [n 64
        ys (trend-signal n 100.0 0.25 7.0 5 0.6)
        model (predict/fit ys 32)]          ; n/2 -> keep every positive bin
    (testing "reconstruction inside the window is exact"
      (doseq [i (range n)]
        (is (< (Math/abs (- (predict/predict-at model i) (nth ys i))) 1e-6))))))

(deftest extrapolation-matches-continuation-of-a-periodic-signal
  ;; A trend-free signal centred in the window has zero linear coupling, so the
  ;; model extends exactly and the continuation is the true periodic value.
  (let [n 64
        a 120.0
        c (/ (- n 1) 2.0)
        spec [[5 7.0] [3 2.5] [8 1.2]]
        ys (mapv #(periodic-at n a spec c %) (range n))
        model (predict/fit ys 32)]
    (doseq [t [n (+ n 10) (+ n 24)]]
      (is (< (Math/abs (- (predict/predict-at model t) (periodic-at n a spec c t))) 1e-6)))))
