(ns qimono.harvest
  (:gen-class)
  (:import [java.math BigDecimal RoundingMode]))

;; Qimono 50% harvest calculator.
;;
;; H50 = RoundDown_Binance(((U * P) - A) / (2 * P))

(defn bd [s] (BigDecimal. (str s)))

(defn round-down-to-step [quantity step]
  (let [n (.divide quantity step 0 RoundingMode/DOWN)]
    (.multiply n step)))

(defn calculate [current position anchor target-profit step]
  (let [market-value (.multiply position current)
        threshold (.add anchor target-profit)]
    (if (< (.compareTo market-value threshold) 0)
      {:eligible false
       :market-value market-value
       :threshold threshold
       :target (bd "0")}
      (let [excess-value (.subtract market-value anchor)
            calculated (.divide excess-value current 18 RoundingMode/HALF_UP)
            half (.divide calculated (bd "2") 18 RoundingMode/HALF_UP)
            target (round-down-to-step half step)]
        {:eligible true
         :market-value market-value
         :threshold threshold
         :calculated calculated
         :target target}))))

(defn -main [& _]
  (println "Qimono harvest REPL")
  (println "Example:")
  (println "(calculate (bd 12345) (bd 0.250) (bd 3055.3875) (bd 0.01) (bd 0.000001))"))
