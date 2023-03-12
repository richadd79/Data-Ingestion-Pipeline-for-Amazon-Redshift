import configparser

# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_invoices_table_drop = "DROP TABLE IF EXISTS staging_invoices"
staging_items_table_drop = "DROP TABLE IF EXISTS staging_items"
imvoices_table_drop = "DROP TABLE IF EXISTS invoices"
items_table_drop = "DROP TABLE IF EXISTS items"

# CREATE TABLES

staging_invoices_table_create = ("""CREATE TABLE IF NOT EXISTS staging_invoices(customerID TEXT, 
                       country TEXT,
                       invoicedate DATE,
                       invoiceno TEXT
                       );""")

staging_items_table_create = ("""CREATE TABLE IF NOT EXISTS staging_items(stockcode TEXT, 
                       description TEXT,
                       unitprice DECIMAL(6,2),
                       quantity INT,
                       invoiceno TEXT
                       );""")


invoices_table_create = ("""CREATE TABLE IF NOT EXISTS invoices (customerid TEXT PRIMARY KEY,
                       country      TEXT,
                       invoicedate  DATE,
                       invoiceno    TEXT);""")

items_table_create = ("""CREATE TABLE IF NOT EXISTS items (stockcode TEXT PRIMARY KEY,
                       description   TEXT,
                       unitprice     DECIMAL(6,2) NOT NULL,
                       quantity      INT,
                       invoiceno     TEXT);""")


# COPY INTO STAGING TABLES

staging_invoices_copy = ("""COPY staging_invoices
                            FROM {}
                            iam_role {}
                            FORMAT AS json 'auto';
                            """).format(config['S3']['INVOICES_DATA'], config['IAM_ROLE']['ARN'], config['S3']['INVOICES_JSONPATH'])


items_invoices_copy = ("""COPY staging_items
                            FROM {}
                            iam_role {}
                            FORMAT AS json 'auto';
                            """).format(config['S3']['ITEMS_DATA'], config['IAM_ROLE']['ARN'], config['S3']['ITEMS_JSONPATH'])

# FINAL TABLES

invoices_table_insert = ("""INSERT INTO invoices (customerid,country,invoicedate,invoiceno)
                            SELECT customerid AS customerid,
                            country AS country,
                            invoicedate AS invoicedate,
                            invoiceno AS invoiceno
                            FROM staging_invoices;""")

items_table_insert = ("""INSERT INTO items (stockCode,description,unitprice,quantity,invoiceno)
                         SELECT stockcode AS stockcode,
                         description AS description,
                         unitprice AS unitprice,
                         quantity AS quantity,
                         invoiceno AS invoiceno
                         FROM staging_items;""")


# QUERY LISTS

create_table_queries = [staging_invoices_table_create, staging_items_table_create, invoices_table_create, items_table_create]
drop_table_queries = [staging_invoices_table_drop, staging_items_table_drop, imvoices_table_drop, items_table_drop]
copy_table_queries = [staging_invoices_copy, items_invoices_copy]
insert_table_queries = [invoices_table_insert,items_table_insert]






