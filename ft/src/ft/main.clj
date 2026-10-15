(ns ft.main
  "CLI: forecast each symbol with the Fourier model and score it on a holdout."
  (:require [clojure.string :as str]
            [ft.data :as data]
            [ft.predict :as predict]
            [ft.metrics :as metrics]))

(def defaults
  {:data "../samples/trading_data.csv"
   :window 512
   :horizon 24
   :k 8
   :out nil})

(defn parse-args
  "Parse --flag value pairs; unknown flags are ignored."
  [args]
  (loop [xs (seq args) opts defaults]
    (if-let [[flag v & more] xs]
      (let [opts (case flag
                   "--data" (assoc opts :data v)
                   "--window" (assoc opts :window (Long/parseLong v))
                   "--horizon" (assoc opts :horizon (Long/parseLong v))
                   "--k" (assoc opts :k (Long/parseLong v))
                   "--out" (assoc opts :out v)
                   opts)]
        (recur (seq (if (contains? #{"--data" "--window" "--horizon" "--k" "--out"} flag)
                      more (cons v more)))
               opts))
      opts)))

(defn- r6 [x] (/ (Math/round (* (double x) 1000000.0)) 1000000.0))

(defn analyse
  "Evaluate one symbol: holdout errors on the last `horizon` points, plus a
   genuine forward forecast refit on the most recent `window` points."
  [{:keys [window horizon k]} {:keys [symbol close]}]
  (let [total (count close)
        split (- total horizon)
        train (subvec (vec close) (- split window) split)
        test (subvec (vec close) split total)
        model (predict/fit train k)
        holdout (predict/predict-series model window horizon)
        recent (subvec (vec close) (- total window) total)
        fmodel (predict/fit recent k)
        forecast (predict/predict-series fmodel window horizon)
        top-periods (->> (:bins model) (map (fn [{:keys [k mag period]}]
                                              {:k k :period_hours (r6 period) :mag (r6 mag)})))]
    {:symbol symbol
     :samples total
     :window window
     :horizon horizon
     :trend_per_hour (r6 (:b model))
     :top_components top-periods
     :holdout {:mae (r6 (metrics/mae test holdout))
               :rmse (r6 (metrics/rmse test holdout))
               :mape_pct (r6 (metrics/mape test holdout))
               :last_actual (r6 (last test))
               :last_predicted (r6 (last holdout))}
     :forecast_next_hours (mapv r6 forecast)}))

(defn- esc [s] (str/replace (str s) "\"" "\\\""))

(defn ->json
  "Hand-rolled JSON for the report (numbers already rounded)."
  [results]
  (let [sym-json
        (fn [{:keys [symbol samples window horizon trend_per_hour top_components holdout forecast_next_hours]}]
          (str "    {"
               "\"symbol\":\"" (esc symbol) "\","
               "\"samples\":" samples ","
               "\"window\":" window ","
               "\"horizon\":" horizon ","
               "\"trend_per_hour\":" trend_per_hour ","
               "\"top_components\":["
               (str/join "," (map (fn [{:keys [k period_hours mag]}]
                                    (str "{\"k\":" k ",\"period_hours\":" period_hours ",\"mag\":" mag "}"))
                                  top_components))
               "],"
               "\"holdout\":{"
               "\"mae\":" (:mae holdout) ","
               "\"rmse\":" (:rmse holdout) ","
               "\"mape_pct\":" (:mape_pct holdout) ","
               "\"last_actual\":" (:last_actual holdout) ","
               "\"last_predicted\":" (:last_predicted holdout) "},"
               "\"forecast_next_hours\":[" (str/join "," forecast_next_hours) "]"
               "}"))]
    (str "{\n"
         "  \"model\":\"detrended-radix2-fft\",\n"
         "  \"results\":[\n" (str/join ",\n" (map sym-json results)) "\n  ]\n}\n")))

(defn -main [& args]
  (let [{:keys [data out] :as opts} (parse-args args)]
    (println "FT — Fourier price-prediction exercise")
    (println "data:" data "| window:" (:window opts) "| horizon:" (:horizon opts) "| k:" (:k opts))
    (println)
    (let [rows (data/load-rows data)
          syms (data/symbols rows)
          results (mapv #(analyse opts (data/series-for rows %)) syms)]
      (doseq [r results]
        (println (format "%-8s  holdout MAE=%-10s RMSE=%-10s MAPE=%-7s%%  trend/h=%s"
                         (:symbol r)
                         (:mae (:holdout r))
                         (:rmse (:holdout r))
                         (:mape_pct (:holdout r))
                         (:trend_per_hour r)))
        (println (format "          top periods (h): %s"
                         (str/join ", " (map :period_hours (:top_components r)))))
        (println (format "          forecast next %d h: %s"
                         (:horizon r) (pr-str (:forecast_next_hours r))))
        (println))
      (when out
        (spit out (->json results))
        (println "wrote JSON report ->" out)))))
