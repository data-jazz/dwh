import snowflake.connector
import configparser

parser = configparser.ConfigParser()
parser.read("config/pipeline.conf")

username = parser.get("snowflake_creds","username")
password = parser.get("snowflake_creds","password")
account_name = parser.get("snowflake_creds","account_name")
warehouse = parser.get("snowflake_creds","warehouse")
database = parser.get("snowflake_creds","database")
schema = parser.get("snowflake_creds","schema")
stage_name = parser.get("snowflake_creds","stage_name")
stage_file_path = parser.get("snowflake_creds","stage_file_path")
target_table = parser.get("snowflake_creds","target_table")

snow_conn = snowflake.connector.connect(
 user = username,
 password = password,
 account = account_name,
 warehouse=warehouse,
 database=database,
 schema=schema,
 stage_name = stage_name,
 stage_file_path = stage_file_path,
 target_table = target_table


 )


# # Connect to Snowflake
# def connect_to_snowflake():
#     try:
#         conn = snowflake.connector.connect(
#             user=username,
#             password=password,
#             account=account_name,
#             warehouse=warehouse,
#             database=database,
#             schema=schema
#         )
#         print("Connected to Snowflake successfully!")
#         return conn
#     except Exception as e:
#         print(f"Failed to connect to Snowflake: {e}")
#         return None

# connect_to_snowflake()


# sql = """COPY INTO people_in_space
#  FROM @my_gcs_stage
#  pattern='.*export.*.csv';"""

sql = f"""
 COPY INTO {target_table}
 FROM {stage_name}/{stage_file_path};
 """


cur = snow_conn.cursor()
cur.execute(sql)
cur.close()
