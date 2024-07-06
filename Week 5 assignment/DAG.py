from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import pyarrow.parquet as pq
import fastavro

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 22),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'database_to_file_format_pipeline',
    default_args=default_args,
    description='A simple data pipeline to export data to CSV, Parquet, and Avro formats',
    schedule_interval=timedelta(days=1),
)

def extract_data():
    # Implement data extraction logic here
    pass

def export_to_csv():
    df = pd.read_sql('SELECT * FROM source_table', conn)
    df.to_csv('/path/to/destination/source_table.csv', index=False)

def export_to_parquet():
    df = pd.read_sql('SELECT * FROM source_table', conn)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, '/path/to/destination/source_table.parquet')

def export_to_avro():
    df = pd.read_sql('SELECT * FROM source_table', conn)
    records = df.to_dict('records')
    with open('/path/to/destination/source_table.avro', 'wb') as out:
        fastavro.writer(out, schema, records)

t1 = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

t2 = PythonOperator(
    task_id='export_to_csv',
    python_callable=export_to_csv,
    dag=dag,
)

t3 = PythonOperator(
    task_id='export_to_parquet',
    python_callable=export_to_parquet,
    dag=dag,
)

t4 = PythonOperator(
    task_id='export_to_avro',
    python_callable=export_to_avro,
    dag=dag,
)

t1 >> [t2, t3, t4]
