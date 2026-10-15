(ns ft.fft-test
  (:require [clojure.test :refer [deftest is testing]]
            [ft.fft :as fft])
  (:import [org.apache.commons.math3.complex Complex]))

(deftest power-of-two-tests
  (testing "recognises powers of two"
    (is (fft/power-of-two? 1))
    (is (fft/power-of-two? 2))
    (is (fft/power-of-two? 512))
    (is (fft/power-of-two? 1024)))
  (testing "rejects non powers of two"
    (is (not (fft/power-of-two? 0)))
    (is (not (fft/power-of-two? 3)))
    (is (not (fft/power-of-two? 1000)))))

(deftest forward-detects-sinusoid-frequency
  (let [n 8
        f 2
        xs (mapv #(Math/cos (/ (* 2.0 Math/PI f %) n)) (range n))
        spectrum (fft/forward xs)
        top (first (fft/top-bins spectrum 1))]
    (is (= 8 (count spectrum)))
    (testing "the strongest positive-frequency bin is the injected one"
      (is (= f (:k top))))))

(deftest forward-rejects-bad-length
  (is (thrown-with-msg? clojure.lang.ExceptionInfo #"power of two"
                        (fft/forward [1.0 2.0 3.0]))))

(deftest magnitudes-of-known-vector
  ;; a real constant has all energy in DC
  (let [spectrum (fft/forward [5.0 5.0 5.0 5.0])
        mags (fft/magnitudes spectrum)]
    (is (< (Math/abs (- (nth mags 0) 20.0)) 1e-9))
    (is (< (nth mags 1) 1e-9))))
