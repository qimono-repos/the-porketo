(ns ft.metrics
  "Forecast error metrics." )

(defn mae
  "Mean absolute error."
  [actual pred]
  (let [n (count actual)]
    (/ (reduce + 0.0 (map (fn [a p] (Math/abs (- (double a) (double p)))) actual pred)) n)))

(defn rmse
  "Root mean squared error."
  [actual pred]
  (let [n (count actual)]
    (Math/sqrt (/ (reduce + 0.0 (map (fn [a p] (let [d (- (double a) (double p))] (* d d))) actual pred)) n))))

(defn mape
  "Mean absolute percentage error (%). Zero actuals are skipped."
  [actual pred]
  (let [pairs (remove (fn [[a _]] (zero? (double a))) (map vector actual pred))
        n (count pairs)]
    (if (zero? n)
      0.0
      (* 100.0 (/ (reduce + 0.0 (map (fn [[a p]] (Math/abs (/ (- (double p) (double a)) (double a)))) pairs)) n)))))
