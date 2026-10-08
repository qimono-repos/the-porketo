(ns porketo.server
  (:require [cheshire.core :as json]
            [compojure.core :refer [GET defroutes]]
            [compojure.route :as route]
            [ring.adapter.jetty :refer [run-jetty]]
            [ring.util.response :as response]
            [porketo.mongo.config :as config]
            [porketo.mongo.db :as db]
            [porketo.mongo.repository :as repo])
  (:gen-class))

(defn json-response [value]
  (-> (response/response (json/generate-string value))
      (response/content-type "application/json")))

(defn routes [database]
  (defroutes app
    (GET "/health" []
      (json-response {:ok true :service "porketo-mongo"}))
    (GET "/lots" []
      (json-response (repo/list-active-lots database)))
    (GET "/lots/:lot-id" [lot-id]
      (if-let [lot (repo/find-lot database lot-id)]
        (json-response lot)
        (-> (json-response {:error "lot not found"}) (response/status 404))))
    (GET "/harvest-events" []
      (json-response (repo/latest-harvest-events database 20)))
    (GET "/balances/:asset" [asset]
      (if-let [balance (repo/latest-balance database asset)]
        (json-response balance)
        (-> (json-response {:error "balance not found"}) (response/status 404))))
    (route/not-found (json/generate-string {:error "not found"}))))

(defn -main [& _]
  (let [cfg (config/config)
        database (db/connect cfg)
        host (or (System/getenv "HOST") "127.0.0.1")
        port (Integer/parseInt (or (System/getenv "PORT") "8080"))]
    (db/ping! database)
    (println (format "porketo-mongo listening on http://%s:%d" host port))
    (run-jetty (routes database) {:host host :port port :join? true})))