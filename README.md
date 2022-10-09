# Spark and Amazon AWS Project

## download_data.py 
In this script I downloaded data on s3 using boto.
```
s3 = boto3.client('s3', aws_access_key_id = ' ', aws_secret_access_key = ' ')

s3.download_file('fatihtuna-case', 'e-commerce.zip', 'brazilian-ecommerce/e-commerce.zip')
```
## write_to_another_folder.py
In this script, I unzipped the downloaded data and wrote it to another folder for next jobs.
```
with zipfile.ZipFile('brazilian-ecommerce/e-commerce.zip', 'r') as zip_ref:
    zip_ref.extractall('data_for_next_job')

with zipfile.ZipFile('brazilian-ecommerce/e-commerce.zip', 'r') as zip_ref:
    zip_ref.extractall('brazilian-ecommerce')
```
## sellers.py
In this script I used spark to query which sellers missed their orders deadline and writed it to a csv file.
```
spark = SparkSession.builder.getOrCreate()

orders_dataset = spark.read.format("csv").option("header", "true").load("brazilian-ecommerce/archive/olist_orders_dataset.csv")
sellers_dataset = spark.read.format("csv").option("header", "true").load("brazilian-ecommerce/archive/olist_sellers_dataset.csv")
items_dataset = spark.read.format("csv").option("header", "true").load("brazilian-ecommerce/archive/olist_order_items_dataset.csv")

orders_dataset.createOrReplaceTempView('orders')
sellers_dataset.createOrReplaceTempView('sellers')
items_dataset.createOrReplaceTempView('items')

sql_query = """SELECT DISTINCT sellers.seller_id, sellers.seller_zip_code_prefix, sellers.seller_city, sellers.seller_state
FROM items JOIN orders ON items.order_id = orders.order_id JOIN sellers ON items.seller_id = sellers.seller_id
WHERE items.shipping_limit_date < orders.order_delivered_carrier_date"""

sellers = spark.sql(sql_query)

sellers.toPandas().to_csv("sellers/sellers.csv", header = True)
```
## upload_output.py
In this script, I uploaded the list of sellers that missed the deadline to s3.
```
import boto3

s3 = boto3.client('s3', aws_access_key_id = ' ', aws_secret_access_key = ' ')

s3.upload_file('sellers/sellers.csv', 'fatihtuna-case', 'sellers/sellers.csv')
```

## Video of the project
https://www.youtube.com/watch?v=jSrs_pY8cUw&ab_channel=FatihTuna

In this video I showed how the project works.
