#!/usr/bin/env bb
;; Qimono Trading harvest calculator.
;;
;; Canonical rule:
;;
;;   V    = U * P
;;   E    = V - A
;;   H    = E / P
;;   H50  = floor_to_binance_step(H / 2)
;;
;; This is a PRE-TRADE TARGET calculator.
;; It does not query Binance or place orders.

(import '[java.math BigDecimal RoundingMode])

(defn bd [s]
  (BigDecimal. (str s)))

(defn round-down-to-step [quantity step]
  (when (<= (.signum step) 0)
    (throw (ex-info "Binance step must be greater than zero" {})))
  (if (<= (.signum quantity) 0)
    (bd "0")
    (let [n (.divide quantity step 0 RoundingMode/DOWN)]
      (.multiply n step))))

(defn harvest-target [position current-price material-anchor binance-step]
  (when (or (<= (.signum position) 0)
            (<= (.signum current-price) 0))
    (throw (ex-info "position and current price must be greater than zero" {})))
  (let [market-value (.multiply position current-price)
        excess-value (.subtract market-value material-anchor)]
    (if (<= (.signum excess-value) 0)
      {:market-value market-value
       :excess-value excess-value
       :calculated-excess (bd "0")
       :target (bd "0")}
      (let [calculated-excess
            (.divide excess-value current-price 30 RoundingMode/HALF_UP)
            half-target
            (.divide calculated-excess (bd "2") 30 RoundingMode/HALF_UP)
            target
            (round-down-to-step half-target binance-step)]
        {:market-value market-value
         :excess-value excess-value
         :calculated-excess calculated-excess
         :target target}))))

(defn parse-args [args]
  (loop [xs args
         result {}]
    (if (empty? xs)
      result
      (let [[flag value & rest] xs]
        (recur rest
               (assoc result
                      (keyword (subs flag 2))
                      value))))))

(defn -main [& args]
  (let [{:keys [to current position anchor step]} (parse-args args)]
    (doseq [[k v] [["--to" to]
                   ["--current" current]
                   ["--position" position]
                   ["--anchor" anchor]
                   ["--step" step]]]
      (when (nil? v)
        (throw (ex-info (str "missing required argument " k) {}))))
    (let [symbol (clojure.string/upper-case to)
          result (harvest-target
                  (bd position)
                  (bd current)
                  (bd anchor)
                  (bd step))
          target (:target result)
          url (str "https://www.binance.com/en/convert/" symbol "/USDT")]
      (println "asset:             " symbol)
      (println "position:          " position)
      (println "current price:     " current)
      (println "material anchor:   " anchor)
      (println "market value:      " (:market-value result))
      (println "excess value:      " (:excess-value result))
      (println "calculated excess: " (:calculated-excess result) symbol)
      (println "50% target:        " target symbol)
      (if (<= (.signum target) 0)
        (println "WAIT: no executable harvest target.")
        (println "GO TO" url "; sell" target symbol "for USDT")))))

(apply -main *command-line-args*)
