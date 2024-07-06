-- Extract data to CSV format
COPY (SELECT * FROM source_table) TO '/path/to/destination/source_table.csv' WITH CSV HEADER;

-- Extract data to Parquet format (using external tools like Apache Spark)
-- Example with PySpark:
# from pyspark.sql import SparkSession
# spark = SparkSession.builder.appName("ExportToParquet").getOrCreate()
# df = spark.read.format("jdbc").option("url", "jdbc:postgresql://hostname:port/dbname").option("dbtable", "source_table").option("user", "username").option("password", "password").load()
# df.write.parquet("/path/to/destination/source_table.parquet")

-- Extract data to Avro format (using external tools like Apache Spark)
# df.write.format("avro").save("/path/to/destination/source_table.avro")
