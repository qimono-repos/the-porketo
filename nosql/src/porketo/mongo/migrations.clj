(ns porketo.mongo.migrations
  (:require [porketo.mongo.config :as config]
            [porketo.mongo.db :as db])
  (:import [com.mongodb.client.model IndexOptions Indexes]))

(defn ensure-indexes! [{:keys [db]}]
  (let [idx (fn [collection keys & {:keys [unique]}]
              (.createIndex (db/collection db collection)
                            keys
                            (cond-> (IndexOptions.)
                              unique (.unique true))))]
    (idx "portfolio_lots" (Indexes/ascending "lotId") :unique true)
    (idx "portfolio_lots" (Indexes/ascending "ticker" "status" "entryPrice"))
    (idx "trades" (Indexes/ascending "tradeId") :unique true)
    (idx "trades" (Indexes/descending "eventNo" "executedAt"))
    (idx "investment_events" (Indexes/ascending "eventNo") :unique true)
    (idx "harvest_events" (Indexes/ascending "eventNo") :unique true)
    (idx "harvest_events" (Indexes/ascending "selectedTicker")
         :unique false)
    (idx "balances" (Indexes/ascending "asset")
         :unique false)
    (idx "prices" (Indexes/ascending "ticker")
         :unique false)
    (idx "reconciliation_events" (Indexes/ascending "asset")
         :unique false)
    (idx "migration_runs" (Indexes/ascending "runId") :unique true))
  :done)

(defn -main [& _]
  (let [connection (db/connect (config/config))]
    (try
      (ensure-indexes! connection)
      (println "MongoDB indexes ensured.")
      (finally (db/close! connection)))))