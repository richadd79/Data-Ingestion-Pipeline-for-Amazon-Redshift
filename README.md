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
Since the data was already cleaned split into Invoices and Items(Products), it was a simple translation of the two datasets into two staging tables
which are STAGING_INVOICES and STAGING_ITEMS.

# ETL Pipeline
This is how the ETL pipeline for Redshift works. The ETL pipeline reads the json-formatted invoices and items data from the S3 Bucket, 
into defined staging tables in Redshift, then proceeds to process it and loads then in their respective analytical tables.


# How to Run




