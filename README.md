# Pengumpulan Data Sensor IoT dengan Apache Kafka
| Nama | NRP |
| ------ | ------ |
| Jeany Aurellia Putri Dewati | 5027221008 |
| Clara Valentina | 5027221016 |

## Studi Kasus Sederhana:
  - Pabrik membutuhkan aliran data sensor yang dapat diteruskan ke layanan analitik atau dashboard secara langsung.
  - Apache Kafka akan digunakan untuk menerima dan mengalirkan data suhu, sementara PySpark akan digunakan untuk mengolah dan memfilter data tersebut.

## Tugas:
1. Buat Topik Kafka untuk Data Suhu:
    - Buat topik di Apache Kafka bernama "sensor-suhu" yang akan menerima data suhu dari sensor-sensor mesin.
2. Simulasikan Data Suhu dengan Producer:
    - Buat producer sederhana yang mensimulasikan data suhu dari beberapa sensor mesin (misalnya, 3 sensor berbeda).
    - Setiap data suhu berisi ID sensor dan suhu saat ini (misalnya, sensor_id: S1, suhu: 70°C), dan dikirim setiap detik ke topik "sensor-suhu".
3. Konsumsi dan Olah Data dengan PySpark:
    - Buat consumer di PySpark yang membaca data dari topik "sensor-suhu".
    - Filter data suhu yang berada di atas 80°C, sebagai indikator suhu yang perlu diperhatikan.
4. Output dan Analisis:
    - Cetak data yang  suhu-nya melebihi 80°C sebagai tanda peringatan sederhana di console.
  
## Langkah Pengerjaan
Sebelum menjalankan program dilakukan langkah persiapan atau setup docker kafka terlebih dahulu. Berikut merupakan langkah untuk melakukan setup.
1. Pertama buat file `docker-compose.yml` yang berisi [code ini](https://github.com/clara-4/bigdata-PysparkKafka/blob/master/docker-compose.yml).
2. Setelah itu jalankan command `sudo docker compose -f docker-compose.yml up -d` pada terminal anda. Hasilnya akan muncul seperti ini.
![WhatsApp Image 2024-11-04 at 13 51 26_3fe6e2ea](https://github.com/user-attachments/assets/0fdcb49f-2503-4d0d-9b6b-d2b7f088b516)
4. Setelah itu jalankan kafka dengan menambahkan topic menggunakan command ```docker exec -it kafka kafka-topics.sh --create --topic sensor-suhu --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1```. Hasil dari command ini akan seperti ini :
![WhatsApp Image 2024-11-04 at 13 51 53_1bcdcaf5](https://github.com/user-attachments/assets/c4449841-6ab6-4d54-83ec-a22e841010b9)

Setelah berhasil menjalankan docker, kita masih memerlukan setup lagi untuk menjalankan produser dan consumer. Dalam hal ini kita memerlukan :
1. Instalasi Python dengan menggunakan `sudo apt-get install python3`
2. Instalasi environtment python3 menggunakan `sudo apt install python3-venv`
3. Instalasi java dengan `sudo apt install default-jdk`
4. Lalu lakukan pemasangan java dengan
   ```
    export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
    echo "export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64" >> ~/.bashrc
    source ~/.bashrc
    echo $JAVA_HOME
   ```
6. Memasang environment python3 dengan `python3 -m venv venv` dan mengaktifkannya dengan `source venv/bin/activate`
7. Didalam environtment python lakukan instalasi pyspark dengan `pip install pyspark` dan kafka-python dengan `pip install kafka-python`

Setelah melakukan setup, kita dapat membuat file [produser.py](https://github.com/clara-4/bigdata-PysparkKafka/blob/master/kafka/temperature_producer.py) dan [consumer.py](https://github.com/clara-4/bigdata-PysparkKafka/blob/master/kafka/pyspark_consumer.py). Kita dapat menjalankan kedua file tersebut pada terminal yang berbeda di dalam environment python dengan command `python3 produser.py` dan `python3 consumer.py`. Setelah dijalankan maka akan muncul output seperti ini :

**File Produser**

![WhatsApp Image 2024-11-04 at 13 58 47_8cab94cf](https://github.com/user-attachments/assets/90a0175a-a7d4-411d-9b38-7575233bb04f)

**File consumer**

![WhatsApp Image 2024-11-04 at 13 29 57_1ca468d5](https://github.com/user-attachments/assets/0598c4dc-dd4a-46c4-9807-d55abb2bbdbd)
