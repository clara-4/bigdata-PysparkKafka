import time
import random
from confluent_kafka import Producer

# Konfigurasi Kafka
conf = {
    'bootstrap.servers': 'localhost:9092'
}
producer = Producer(conf)

# Fungsi untuk mengirim data
def send_temperature_data():
    sensor_ids = ['S1', 'S2', 'S3']
    while True:
        for sensor_id in sensor_ids:
            temperature = random.randint(60, 100)  # Suhu acak antara 60 dan 100
            data = f"{sensor_id},{temperature}"
            producer.produce('sensor-suhu', value=data)
            print(f"Data dikirim: {data}")
        producer.flush()
        time.sleep(1)  # Kirim setiap detik

send_temperature_data()
