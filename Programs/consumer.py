from kafka import KafkaConsumer
from json import loads
from files import *
import pprint

consumer = KafkaConsumer(
    'file-input',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     auto_commit_interval_ms=1000,
     group_id='output-test',
     value_deserializer=lambda x: loads(x.decode('utf-8')),
     consumer_timeout_ms = 1000
     )

files= {}
DIR = ''
recursion = 'y'
extension = ''
try:
    for msg in consumer:
        print(msg)
        DIR = msg.value[0]
        recursion = msg.value[1]
        extension = msg.value[2]
        files = find_details(DIR, files, recursion)
except NotADirectoryError:
    print("The location you provided was not a directory")
    consumer.close()
    exit()
except FileNotFoundError:
    print("The directory or file was not found")
    consumer.close()
    exit()

length = number_of_file(files)
print(f"Number of files in directory is {length}")

extension_number = number_of_extension(files, extension)
print(f"Number of files with the extension {extension} are {extension_number}")

try:
    sizes = size(files)
except NameError:
    print("Directory is Empty")
else:
    print(f"Largest file is {sizes[0][0]} in {sizes[0][1]} with size {sizes[0][2]}")
    print(f"Smallest file is {sizes[1][0]} in {sizes[1][1]} with size {sizes[1][2]}")

try:
    mod_date = modify(files)
except NameError:
    print("Directory is Empty")
else:
    print(f"Most recently modified file is {mod_date[0]} in {mod_date[1]} with time {mod_date[2]}")

details = input("Do you want more insights on the files?\t")
if details == 'y' or details == 'Y':
    pprint.pprint(files)