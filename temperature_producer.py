from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

sensors = ['S1', 'S2', 'S3']

while True:
    sensor_data = {
        'sensor_id': random.choice(sensors),
        'suhu': random.uniform(60, 100)  # Simulasikan suhu antara 60°C dan 100°C
    }
    producer.send('sensor-suhu', sensor_data)
    print(f"Mengirim: {sensor_data}")
    time.sleep(1)  # Kirim data setiap detik
