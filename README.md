# Automated Weather ETL Pipeline with Python, PostgreSQL, and Airflow

## Project Objective
This project simulates the role of a Data Engineer by designing and implementing an automated ETL (Extract, Transform, Load) pipeline for weather data. The pipeline extracts raw weather data from the OpenWeatherMap API, cleans and transforms it, and loads it into a PostgreSQL database. All steps are orchestrated using Apache Airflow, following end-to-end data engineering best practices.

Key goals:
- Automate the ingestion and processing of weather data
- Ensure data quality and consistency through cleaning and transformation
- Store processed data in a relational database, ready for further data analysis with SQL or Python, or for visualization with tools such as matplotlib
- Showcase orchestration and scheduling with Airflow

## Dataset
**Source:** [OpenWeatherMap One Call API](https://openweathermap.org/api/one-call-3)

- Real-time and historical weather data for Rome, Italy
- Fields include: temperature, humidity, wind, weather conditions, hourly and daily forecasts, and more
- Data is retrieved in JSON format and processed into structured tables

## Project Architecture & Tools

The project implements a robust ETL pipeline using industry-standard tools and practices:

1. **Extraction:**  
   - Python script (`extract.py`) fetches weather data from the OpenWeatherMap API using HTTP requests
   - Raw JSON data is saved locally for reproducibility and downstream processing

2. **Cleaning & Transformation:**  
   - Python script (`clean_transform.py`) reads raw JSON, normalizes nested structures, and handles missing or inconsistent values
   - Data is split into raw, hourly, and daily tables, and exported as CSV for loading

3. **Loading:**  
   - Python script (`load.py`) loads the cleaned data into PostgreSQL tables using SQLAlchemy and pandas
   - Ensures schema consistency and handles table creation/replacement

4. **Orchestration:**  
   - Apache Airflow DAG (`weather_etl_dag.py`) schedules and manages the ETL workflow
   - Each ETL step is a separate Airflow task, enabling monitoring and retry logic

5. **Configuration:**  
   - Database and API credentials are managed in a separate config file (`db_config.py`)

## Data Engineering Outcomes
With the processed weather data in PostgreSQL, the dataset is ready for further data analysis using SQL or Python, or for visualization with your preferred tool (e.g., matplotlib).  
If you are interested in my data analysis and data visualization skills, see my other project: [dataAnalysis - eCommerce](https://github.com/Andrii04/dataAnalysis-eCommerce).

Example questions that can be addressed include:
- What are the daily and hourly weather trends in Rome?
- How do temperature, humidity, and other metrics change over time?
- Can we identify patterns or anomalies in weather conditions?

## Technologies Used
- **Python** (`requests`, `pandas`, `sqlalchemy`)
- **PostgreSQL** for relational data storage
- **Apache Airflow** for workflow orchestration and scheduling
- **OpenWeatherMap API** as the data source

## Repository Structure
- `extract.py`: Extracts raw weather data from the API
- `clean_transform.py`: Cleans and transforms raw data into structured tables
- `load.py`: Loads cleaned data into PostgreSQL
- `weather_etl_dag.py`: Airflow DAG for orchestrating the ETL pipeline
- `db_config.py`: Stores database and API credentials
- `romeWeather.csv`, `romeWeatherHourly.csv`, `romeWeatherDaily.csv`: Example output datasets
- `raw_data.json`: Example raw data file
- `airflow_etl_pipeline.png`: Example of DAG run in Airflow
- `README.md`: Project documentation

## Data Source
- [OpenWeatherMap One Call API](https://openweathermap.org/api/one-call-3)

---
