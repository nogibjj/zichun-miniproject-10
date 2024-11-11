from pyspark.sql import SparkSession
from pyspark.sql.functions import hour, col

# Initialize Spark session
spark = SparkSession.builder.appName("NYC_Taxi_Trip_Analysis").getOrCreate()

# Load data
df = spark.read.csv("data/nyc_taxi_trip_data.csv", header=True, inferSchema=True)

# Transformation: Filter for peak hours
df_filtered = df.filter((hour(col("pickup_datetime")).between(7, 9)) | (hour(col("pickup_datetime")).between(16, 18)))

# Add new columns for speed and distance calculations
# Note: Simplified; use actual distance formulas as needed.
df_transformed = df_filtered.withColumn("trip_speed", col("trip_duration") / col("distance"))

# Spark SQL query for hourly average trip duration
df_transformed.createOrReplaceTempView("trips")
hourly_avg = spark.sql("SELECT hour(pickup_datetime) as hour, AVG(trip_duration) as avg_duration FROM trips GROUP BY hour")

hourly_avg.show()
