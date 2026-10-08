(ns porketo.mongo.config
  (:require [environ.core :refer [env]]))

(defn config []
  {:uri (or (env :mongodb-uri)
            (throw (ex-info "MONGODB_URI is required" {})))
   :database (or (env :mongodb-database) "porketo_dev")})