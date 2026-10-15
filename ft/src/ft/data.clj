(ns ft.data
  "Load the synthetic hourly dataset into plain Clojure data."
  (:require [clojure.data.csv :as csv]
            [clojure.java.io :as io]))

(defn load-rows
  "Read a CSV file into a vector of maps keyed by the header row."
  [path]
  (with-open [r (io/reader path)]
    (let [[header & rows] (csv/read-csv r)
          ks (mapv keyword header)]
      (mapv #(zipmap ks %) rows))))

(defn- dbl [s] (Double/parseDouble s))

(defn symbols
  "Distinct symbols in file order."
  [rows]
  (distinct (map :symbol rows)))

(defn series-for
  "Return the full OHLCV series for one symbol, in file order."
  [rows symbol]
  (let [rs (filter #(= symbol (:symbol %)) rows)]
    {:symbol symbol
     :timestamps (mapv :timestamp rs)
     :open (mapv (comp dbl :open) rs)
     :high (mapv (comp dbl :high) rs)
     :low (mapv (comp dbl :low) rs)
     :close (mapv (comp dbl :close) rs)
     :volume (mapv #(Long/parseLong (:volume %)) rs)}))
