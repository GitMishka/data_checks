Data Quality Assurance Project

This project aims to perform data quality checks on a PostgreSQL database. It identifies and reports issues in data like null values, duplicate IDs, negative comments, invalid upvote ratios, and future timestamps. The results are then exported to a CSV file.
Tools/Modules Used

    Python: Core programming language used for the project.
    psycopg2: PostgreSQL database adapter for Python. Used for connecting to PostgreSQL databases, executing SQL commands, and managing transactions.
    pandas: Data manipulation and analysis library. Used for transforming data and handling dataframes.
    datetime: Python's standard library for dealing with dates and times. Used for generating timestamps for reports.

Steps Involved

    Data Extraction: Connect to the PostgreSQL database and execute a SQL query to fetch data.

    Data Quality Check: Perform several quality checks on the extracted data, which include checking for null values, checking for duplicate IDs, checking for negative comment counts, validating upvote ratios, and verifying timestamps.

    Export Report: Convert the results of the data quality check into a dataframe and export it to a CSV file.

How to Run

Run the provided script which will perform all the steps involved in this data quality assurance process. The script will automatically generate a timestamped CSV report with the results.

Note: This project assumes that you have a running PostgreSQL instance and all the necessary Python libraries installed. You also need to provide the appropriate database connection parameters.
