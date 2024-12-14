
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas
import snowflake.connector
import warnings

warnings.filterwarnings(
    action='ignore',
    category=UserWarning,
    module='snowflake.connector'
)

def load(data):
    df_data = data

    # Snowflake connection details
    ACCOUNT = 'vg91524.europe-west2.gcp'
    USER = 'my_user'
    PASSWORD = 'Complete1'
    DATABASE = 'my_db'
    SCHEMA = 'subscriptions'
    WAREHOUSE = 'compute_wh'
    ROLE = 'my_role'
    TABLE_NAME = 'PRODUCT'

    # Connect to Snowflake
    conn = snowflake.connector.connect(
        user=USER,
        password=PASSWORD,
        account=ACCOUNT,
        warehouse=WAREHOUSE,
        database=DATABASE,
        schema=SCHEMA,
        role=ROLE,
    )
    print(f"starting to connect...")
    # Write DataFrame to Snowflake table
    success, nchunks, nrows, _ = write_pandas(conn, df_data, TABLE_NAME)

    # Check the result
    if success:
        print(f"Successfully uploaded {nrows} rows to {TABLE_NAME}.")
    else:
        print("Upload failed.")

    # Close the connection
    conn.close()