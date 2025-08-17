# Description

Database operations exist in this file

## Initialize the Database

This must be done whenever changes are made to schema.sql.

CAUTION: This will delete all data in the database! Use only for a fresh start.

### Steps

1. cd ~/recipefirst/data
2. sqlite3 instances/recipefirst.db < schema.sql

## Patch the Database

patch.sql can be used to insert test data into the database or make live changes to the schema. This option will not delete data in the database but it will also have to adhere to any constraints or relationships that already exist.

### Steps

1. cd ~/recipefirst/data
2. sqlite3 instances/recipefirst.db < patch.sql