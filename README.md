# MySQL and Google Sheets Data Integration

This repository provides a set of scripts to extract data from a MySQL database, transform it into a CSV file, and integrate it with Google Sheets. The workflow includes database connection, querying, data transformation, and file generation.

## Files Overview

### 1. `connect_mysql.py`
- Establishes a connection to a MySQL database.
- Allows querying and data manipulation.
- Key functions:
  - `connect_mysql`: Connects to the database and returns a connection object.

### 2. `credentials.py`
- Manages Google API credentials for accessing Google Sheets.
- Key functions:
  - `credentials`: Loads credentials from a JSON file and returns an authenticated credentials object.

### 3. `id_spreadsheets.py`
- Stores and retrieves the Google Sheets ID for interaction.
- Key functions:
  - `spreadsheets`: Returns the Google Sheets ID.

### 4. `queries.py`
- Defines and executes SQL queries on the connected MySQL database.
- Key functions:
  - `amounts_quantity`: Retrieves data about vehicle circulation permits, including vehicle details, payment type, and service module.

### 5. `sql_to_csv.py`
- Converts query results into a CSV file.
- Key functions:
  - `sql_to_csv`: Transforms SQL query results into a CSV file named `vehicle_circulation_permit.csv`.

## Prerequisites

1. **Python 3.7 or higher**
2. **Dependencies**
   Install required libraries:
   ```bash
   pip install pymysql pandas google-auth google-auth-oauthlib
   ```

3. **Google API Credentials**
   - Obtain a credentials JSON file from the Google Cloud Console.
   - Save it as `credentials.json` in the project directory.

4. **MySQL Database**
   - Ensure your database server is running and the credentials are correct in `connect_mysql.py`.

## Usage

### 1. **Connect to MySQL Database**
   - Update the `connect_mysql` function in `connect_mysql.py` with your database details.

### 2. **Configure Google Sheets**
   - Replace the `SPREADSHEET_ID` in `id_spreadsheets.py` with your Google Sheets ID.

### 3. **Execute Queries**
   - Use `queries.py` to define and execute your SQL queries.
   - Example:
     ```python
     from queries import amounts_quantity
     data = amounts_quantity()
     print(data)
     ```

### 4. **Generate CSV File**
   - Run `sql_to_csv.py` to save query results as a CSV file.
   - Example:
     ```bash
     python sql_to_csv.py
     ```
   - Output: `vehicle_circulation_permit.csv`

## Project Structure

```plaintext
.
├── connect_mysql.py
├── credentials.py
├── id_spreadsheets.py
├── queries.py
├── sql_to_csv.py
├── credentials.json
├── vehicle_circulation_permit.csv
└── README.md
```

## Notes
- Ensure your MySQL server is accessible and credentials are correct.
- For Google Sheets, verify API permissions and access.
- Modify queries in `queries.py` as per your database structure and requirements.

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request for improvements.