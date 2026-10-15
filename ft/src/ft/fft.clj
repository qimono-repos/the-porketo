(ns ft.fft
  "Thin wrapper around Apache Commons Math's radix-2 FastFourierTransformer."
  (:import [org.apache.commons.math3.transform FastFourierTransformer
            DftNormalization TransformType]
           [org.apache.commons.math3.complex Complex]))

(defn power-of-two?
  [n]
  (and (integer? n) (pos? n) (zero? (bit-and (long n) (dec (long n))))))

(def ^:private ^FastFourierTransformer transformer
  (FastFourierTransformer. DftNormalization/STANDARD))

(defn forward
  "Forward FFT of a real-valued sequence. Length must be a power of two.
   Returns a vector of [re im] pairs of the same length."
  [xs]
  (let [n (count xs)]
    (when-not (power-of-two? n)
      (throw (ex-info "FFT length must be a power of two" {:length n})))
    (let [out (.transform transformer (double-array xs) TransformType/FORWARD)]
      (mapv (fn [^Complex c] [(.getReal c) (.getImaginary c)]) out))))

(defn magnitudes
  [spectrum]
  (mapv (fn [[re im]] (Math/hypot re im)) spectrum))

(defn bands
  "Positive-frequency bins k = 1 .. n/2-1 (excludes DC and Nyquist)."
  [spectrum]
  (let [m (magnitudes spectrum)
        n (count spectrum)]
    (mapv (fn [k] {:k k :mag (nth m k) :period (/ (double n) k)})
          (range 1 (quot n 2)))))

(defn top-bins
  "The `k` strongest positive-frequency bins, strongest first."
  [spectrum k]
  (->> (bands spectrum) (sort-by :mag >) (take k) vec))
