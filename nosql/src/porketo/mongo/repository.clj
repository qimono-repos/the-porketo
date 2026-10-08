(ns porketo.mongo.repository
  (:require [porketo.mongo.db :as db])
  (:import [org.bson Document]
           [com.mongodb.client.model Sorts Filters]))

(defn doc->map [^Document doc]
  (when doc (into {} doc)))

(defn list-active-lots [{:keys [db]}]
  (let [cursor (.find (db/collection db "portfolio_lots")
                      (Filters/eq "status" "active"))
        sorted (.sort cursor (Sorts/ascending "ticker" "entryPrice"))]
    (map doc->map (iterator-seq (.iterator sorted)))))

(defn find-lot [{:keys [db]} lot-id]
  (doc->map
   (.first (.find (db/collection db "portfolio_lots")
                  (Filters/eq "lotId" lot-id)))))

(defn latest-harvest-events [{:keys [db]} limit]
  (let [cursor (.find (db/collection db "harvest_events"))
        sorted (.sort cursor (Sorts/descending "eventNo"))
        limited (.limit sorted (int limit))]
    (map doc->map (iterator-seq (.iterator limited)))))

(defn latest-balance [{:keys [db]} asset]
  (doc->map
   (.first
    (.sort
     (.find (db/collection db "balances")
            (Filters/eq "asset" asset))
     (Sorts/descending "capturedAt")))))