
# NYC Taxi Trip Duration Analysis with PySpark

This project uses PySpark to analyze a large dataset of New York City taxi trips. It includes data transformations and SQL queries to extract insights, implementing a CI/CD pipeline for testing and deployment.

## Dataset

**Dataset Name**: New York City Taxi Trip Duration  
**Source**: [Kaggle](https://www.kaggle.com/datasets/new-york-city/nyc-taxi-trip-duration)  
**Description**: The dataset contains details about taxi trips in NYC, including:
- `id`: Unique identifier for each trip
- `pickup_datetime` and `dropoff_datetime`: Start and end times for each trip
- `passenger_count`: Number of passengers in the taxi
- `pickup_longitude`, `pickup_latitude`, `dropoff_longitude`, `dropoff_latitude`: Geographical coordinates of pickup and drop-off locations
- `trip_duration`: Duration of the trip in seconds

Download the dataset from Kaggle, upload it to your repository, and make it accessible in Codespaces.

## Setup with GitHub Codespaces

This project uses GitHub Codespaces, a cloud-based development environment pre-configured with PySpark.

### Step 1: Launch GitHub Codespaces

1. Go to your GitHub repository, click on the `Code` button, select `Codespaces`, and click `Create codespace on main`.

### Step 2: Verify PySpark Installation

Most Codespaces images have PySpark pre-installed. Verify the installation with:
```bash
pyspark --version
```

If PySpark isn’t installed, install it using:
```bash
pip install pyspark
```


## Project Structure

The project performs the following tasks on the NYC Taxi dataset:

1. **Data Transformation**  
   - Filters trips to analyze trips during peak hours (e.g., 7-9 AM and 4-6 PM).
   - Creates new columns, such as trip speed and distance based on geographical coordinates.

2. **Spark SQL Queries**  
   - Query 1: Calculate the average trip duration and distance for each hour.
   - Query 2: Analyze popular pickup and drop-off areas by counting trips in various city zones.

## CI/CD Pipeline

This project includes a CI/CD pipeline using GitHub Actions to:
- Run tests on PySpark transformations and SQL queries.
- Ensure that code changes do not introduce errors.

## Installation & Usage

1. **Upload the Dataset**  
   - Download the NYC Taxi dataset from Kaggle and upload it to your Codespace, ideally in a `data` folder.

2. **Run the PySpark Script**  
   - Execute the script in Codespaces:
     ```bash
     spark-submit script.py
     ```

## Deliverables

- **PySpark Script**: `script.py` with data transformation and SQL queries
- **Output Summary Report**: `output_summary.md` showing key insights from the analysis

