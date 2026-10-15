(ns ft.metrics-test
  (:require [clojure.test :refer [deftest is]]
            [ft.metrics :as metrics]))

(deftest mae-basic
  (is (< (Math/abs (- (metrics/mae [1 2 3] [1 2 3]) 0.0)) 1e-12))
  (is (< (Math/abs (- (metrics/mae [1 2 3] [2 4 6]) 2.0)) 1e-9)))

(deftest rmse-basic
  (is (< (Math/abs (- (metrics/rmse [0 0 0] [3 3 3]) 3.0)) 1e-9)))

(deftest mape-basic
  (is (< (Math/abs (- (metrics/mape [100 100] [110 90]) 10.0)) 1e-9))
  (metrics/mape [0 0] [1 1]))
