import json

from kafka import KafkaConsumer
from kafka import KafkaProducer

ORDER_KAKFA_TOPIC = "order_details"
ORDER_CONFIRMED_KAFKA_TOPIC = "order_confirmed"

consumer = KafkaConsumer(
    ORDER_KAKFA_TOPIC,
    bootstrap_servers="localhost:29092"
)
producer = KafkaProducer(
    bootstrap_servers="localhost:29092"
)

print("Gonna start listening...")
# 接收order_backend.py的資料並轉換為json印出
while True:
    for message in consumer:
        print("Ongoing transaction...")
        consumed_message = json.loads(message.value.decode())
        print(consumed_message)

        user_id = consumed_message["user_id"]
        total_cost = consumed_message["total_cost"]

# 將從order_backend.py收到的資料user_id, total_cost 轉換為 custome_id, customer_email, total_cost
# 並發送

        data = {
            "coustomer_id": user_id,
            "customer_email": f"{user_id}@gmail.com",
            "total_cost": total_cost
        }

        print("Successful transaction...")
        producer.send(
            ORDER_CONFIRMED_KAFKA_TOPIC,
            json.dumps(data).encode("utf-8")
        )