(ns porketo.mongo.schema
  "Application-level persistence contracts. MongoDB is document-oriented, so this is a domain schema layer rather than a relational ORM.")

(def collections
  #{:portfolio-lots :trades :investment-events :harvest-events
    :balances :prices :reconciliation-events :policy-snapshots :migration-runs})

(defn require-fields [m fields]
  (doseq [field fields]
    (when-not (contains? m field)
      (throw (ex-info "Missing required field" {:field field :document m}))))
  m)

(defn portfolio-lot [m]
  (require-fields m [:lotId :ticker :assetClass :entryPrice :units :anchor]))

(defn harvest-event [m]
  (require-fields m [:eventNo :scheduledAt :status]))