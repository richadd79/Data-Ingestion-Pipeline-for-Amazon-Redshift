# Introduction
A UK based online retail shop has grown and increased their sales/purchases and decided to move their data and processes onto the cloud.
Their json-formatted data resides in s3 directory, consists of Invoices and Items.

As their data engineer, I was tasked to build an ETL pipeline that extracts the data in s3, stage it in Redshift,and transform
the data into analytical tables for the analytical team for further insights.

Goals for the project:
- Load sales data from S3 to staging tables in Redshift
- Execute SQL Statements to create analytical tables from staging tables

# Dataset
The dataset utilized in this project is from [Online Retail Data Set](https://archive-beta.ics.uci.edu/dataset/502/online+retail+ii)

# Schema Design
Data was already cleaned and split into Invoices and Items(Products), it was a simple translation of the two datasets into two staging tables
which are STAGING_INVOICES and STAGING_ITEMS.

# ETL Pipeline
This is how the ETL pipeline for Redshift works. The ETL pipeline reads the json-formatted invoices and items data from the S3 Bucket, 
into defined staging tables in Redshift, then proceeds to process it and loads then in their respective analytical tables.


# How to Run
First to be able to run this project, a config file needs to be in place as Infrastructure As Code(IAC).
With this configuration contains Cluster details, IAM_ROLE and S3 Bucket directories to the data and jsonpaths.
This IAC file is not included in this repo, but below is the format used
     
     [CLUSTER]
     HOST=''
     DB_NAME=''
     DB_USER=''
     DB_PASSWORD=''
     DB_PORT=5439

     [IAM_ROLE]
     ARN='IAM Role arn'

     [S3]
     INVOICES_DATA='s3://ecom-deng-bkt/invoices/'
     INVOICES_JSONPATH='s3://ecom-deng-bkt/invoices_jsonpaths.json'
     ITEMS_DATA='s3://ecom-deng-bkt/items/'
     ITEMS_JSONPATH='s3://ecom-deng-bkt/items_jsonpaths.json'


#### Now Let's run

     # Run the create_table first to create all tables on Redshift
       python create_table.py
     
     # Run the etl.py to process and load the data to respective analytical tables.
       python etl.py
     

# Resources
[AWS Redshift Documentation](https://aws.amazon.com/redshift/)


