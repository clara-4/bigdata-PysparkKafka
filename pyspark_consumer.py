from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
import json
from pyspark.sql.types import StructType, StructField, StringType, FloatType

# Membuat sesi Spark
spark = SparkSession.builder \
    .appName("KafkaPySparkConsumer") \
    .getOrCreate()

# Membaca data dari Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sensor-suhu") \
    .load()

# Skema untuk data JSON
schema = StructType([
    StructField("sensor_id", StringType(), True),
    StructField("suhu", FloatType(), True)
])

# Mendekode dan memproses data JSON
value_df = df.selectExpr("CAST(value AS STRING)")
json_df = value_df.select(from_json(col("value"), schema).alias("data")).select("data.*")

# Filter suhu yang lebih dari 80°C
alert_df = json_df.filter(col("suhu") > 80)

# Menampilkan data suhu yang perlu diwaspadai
query = alert_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
