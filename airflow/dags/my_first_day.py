from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator \
 import BashOperator
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator

dag = DAG(
 'simple_dag',
 description='A simple DAG',
 schedule_interval=timedelta(days=1),
 start_date = days_ago(1),
#  'email': [bizzyjunky@gmail.com],
#  'email_on_failure': False,
#  'email_on_retry': False,

)
t1 = BashOperator(
 task_id='print_date',
 bash_command='date',
 dag=dag,
)
t2 = BashOperator(
 task_id='sleep',
 depends_on_past=False,
 bash_command='sleep 3',
 dag=dag,
)
t3 = BashOperator(
 task_id='print_end',
 depends_on_past=False,
 bash_command='echo \'end\'',
 dag=dag,
)

email_task = EmailOperator(
 task_id='send_email',
 to="bizzyjunky@gmail.com.com",
 subject="Airflow Test Email",
 html_content='some test content',
 dag=dag,
 )

t1 >> t2
t2 >> t3
t3 >> email_task