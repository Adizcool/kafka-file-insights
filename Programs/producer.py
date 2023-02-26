from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
producer.flush()
DIR = input("Give the directory path\t")
recursion = input("Do you wish to check folders in the location too?\t")
extension = input("Give file extension to search\t")

producer.send('file-input', value = (DIR, recursion, extension))
producer.flush()
producer.close()