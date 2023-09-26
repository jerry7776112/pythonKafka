import json
import time

from kafka import KafkaProducer

ORDER_KAFKA_TOPIC = "order_details"
ORDER_LIMIT = 5

producer = KafkaProducer(bootstrap_servers="localhost:29092")

print("Going to be generating order after 10 seconds")
print("Will generate one unique order every 10 seconds")

# 模擬訂單數據
for i in range(1, ORDER_LIMIT):
    data = {
        "order_id":1,
        "user_id":f"tom_{i}",
        "total_cost": i * 2,
        "items": "burger, sandwich"
    }
# 將數據發送到所定義的主題
    producer.send(
        ORDER_KAFKA_TOPIC,
        json.dumps(data).encode("utf-8")
    )
    print(f"Done sending...{i}")
    time.sleep(10)