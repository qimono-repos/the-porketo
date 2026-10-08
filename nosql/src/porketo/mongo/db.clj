(ns porketo.mongo.db
  (:import [com.mongodb ConnectionString MongoClient MongoClientSettings]
           [com.mongodb.client MongoClients MongoDatabase]
           [org.bson Document]))

(defn connect [{:keys [uri database]}]
  (let [settings (-> (MongoClientSettings/builder)
                     (.applyConnectionString (ConnectionString. uri))
                     (.build))
        client (MongoClients/create settings)]
    {:client client
     :db (.getDatabase client database)}))

(defn close! [{:keys [client]}]
  (.close ^MongoClient client))

(defn ping! [{:keys [db]}]
  (.runCommand ^MongoDatabase db (Document. {"ping" 1}))
  true)

(defn collection [db name]
  (.getCollection ^MongoDatabase db name Document))