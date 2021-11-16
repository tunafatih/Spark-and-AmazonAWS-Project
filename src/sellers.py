from pyspark.sql import SparkSession

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