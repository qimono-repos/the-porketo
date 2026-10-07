(ns harvest
  (:import [java.math BigDecimal RoundingMode]))

;; Qimono Trading 50% harvest calculator.
;; Pre-trade calculator only. It never places an order.
;; Execution truth remains the live Binance conversion receipt.
;;
;; Example:
;; clj -M harvest.clj --harvest --to ETH --current 12345 --position 0.250 --anchor 3055.3875
;;
;; Optional:
;; --target-profit 0.01
;; --step 0.000001

(defn bd [s]
  (BigDecimal. s))

(defn round-down-to-step [quantity step]
  (let [n (.divide quantity step 0 RoundingMode/DOWN)]
    (.multiply n step)))

(defn harvest-target [current position anchor target-profit step]
  (let [market-value (.multiply position current)
        threshold   (.add anchor target-profit)]
    (if (< (.compareTo market-value threshold) 0)
      {:eligible false
       :market-value market-value
       :threshold threshold
       :target (bd "0")}
      (let [excess-value       (.subtract market-value anchor)
            calculated-harvest (.divide excess-value current 18 RoundingMode/HALF_UP)
            half-harvest       (.divide calculated-harvest (bd "2") 18 RoundingMode/HALF_UP)
            target             (round-down-to-step half-harvest step)]
        {:eligible true
         :market-value market-value
         :threshold threshold
         :calculated-harvest calculated-harvest
         :half-harvest half-harvest
         :target target}))))

(defn arg-map [args]
  (loop [xs args m {}]
    (if (empty? xs)
      m
      (let [[k v & more] xs]
        (recur more (assoc m k v))))))

(defn -main [& argv]
  (let [m             (arg-map argv)
        symbol        (or (get m "--to") (throw (ex-info "--to is required" {})))
        current       (bd (or (get m "--current") (throw (ex-info "--current is required" {}))))
        position      (bd (or (get m "--position") (throw (ex-info "--position is required" {}))))
        anchor        (bd (or (get m "--anchor") (throw (ex-info "--anchor is required" {}))))
        target-profit (bd (or (get m "--target-profit") "0.01"))
        step          (bd (or (get m "--step") "0.000001"))
        r             (harvest-target current position anchor target-profit step)
        url           (str "https://www.binance.com/en/convert/" symbol "/USDT")]
    (if-not (= "--harvest" (first argv))
      (throw (ex-info "use --harvest" {})))
    (if-not (:eligible r)
      (do
        (println "WAIT:" symbol "lot has not crossed the harvest criterion.")
        (println "market value =" (:market-value r))
        (println "threshold    =" (:threshold r)))
      (if (<= (.compareTo (:target r) (bd "0")) 0)
        (println "WAIT: calculated 50% harvest is below the executable step.")
        (do
          (println "GO TO" url)
          (println "sell" (:target r) symbol)
          (println "expected proceeds ≈" (.multiply (:target r) current) "USDT")
          (println)
          (println "market value       =" (:market-value r))
          (println "excess value       =" (.subtract (:market-value r) anchor))
          (println "calculated harvest =" (:calculated-harvest r) symbol)
          (println "50% target         =" (:half-harvest r) symbol)
          (println "rounded target     =" (:target r) symbol)
          (println "VERIFY Binance live conversion constraints before execution."))))))

(apply -main *command-line-args*)
