(ns ft.runner
  "Minimal test runner so `clojure -M:test` needs no extra dependencies."
  (:require [clojure.test :as t]
            ft.fft-test
            ft.predict-test
            ft.metrics-test))

(defn -main [& _]
  (let [{:keys [fail error]} (t/run-tests 'ft.fft-test 'ft.predict-test 'ft.metrics-test)]
    (System/exit (if (zero? (+ (long fail) (long error))) 0 1))))
