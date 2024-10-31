from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col

# Membuat sesi Spark
spark = SparkSession.builder \
    .appName("KafkaSensorConsumer") \
    .getOrCreate()

# Membaca data dari topik Kafka
sensor_data = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sensor-suhu") \
    .load()

# Mengubah data menjadi format yang mudah dibaca
sensor_df = sensor_data.selectExpr("CAST(value AS STRING)")
sensor_df = sensor_df.withColumn("sensor_id", split(sensor_df["value"], ",")[0]) \
                     .withColumn("temperature", split(sensor_df["value"], ",")[1].cast("integer"))

# Filter suhu yang melebihi 80°C
filtered_df = sensor_df.filter(col("temperature") > 80)

# Menampilkan hasil
query = filtered_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
