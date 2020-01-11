### Example DAG demonstrating the usage of the PythonOperator ###

import time
from datetime import datetime

from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

args = {
    'owner': 'airflow',
    'start_date': datetime(2019, 1, 1),
}

dag = DAG(
    dag_id='example_python_operator',
    default_args=args,
    schedule_interval=None
)


def print_context(ds, **kwargs):
    pprint(kwargs)
    print(ds)
    return


run_this = PythonOperator(
    task_id='print_the_context',
    python_callable=print_context,
    dag=dag,
)


def my_sleeping_function(num_seconds):
    time.sleep(num_seconds)
    return


# Generate 5 sleeping tasks, tasks will be executed in parallel
for i in range(5):
    task = PythonOperator(
        task_id=f"sleep-for-{5*i}-seconds",
        python_callable=my_sleeping_function,
        op_kwargs={'num_seconds': 5*i,
        dag=dag,
    )

    run_this >> task