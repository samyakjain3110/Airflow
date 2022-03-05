from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.models.baseoperator import chain
from airflow.sensors.filesystem import FileSensor
from datetime import datetime,timedelta

# default_args = {
#     'retry' : 3,
#     'retry_delay' : timedelta(minutes = 1)
# }

def funct():
    return 43

def funct2(ti):
    var = ti.xcom_pull(key="return_value" , task_ids=["python_task"])
    print("got xcom value as :" , var)

with DAG(dag_id="simple_dag",start_date=datetime(2022,1,29),catchup = True) as dag:
    python_task = PythonOperator(
        task_id = "python_task",
        python_callable = funct
        # op_kwargs = {'my_param':24}
    )
    
    get_data = PythonOperator(
        task_id = "get_data",
        python_callable = funct2
    )
    # sensor_task = FileSensor(
    #     task_id='sensor_task',
    #     fs_conn_id='fs_default',
    #     filepath= 'file.txt'
    # )

    # bash_task = BashOperator(
    #     task_id ='bash_task',
    #     bash_command ='printf "path is : %s : %s " $PATH $LS '
    # )

# chain(python_task ,[sensor_task , bash_task])
python_task >> get_data 
cross_downstream([task1,task2],[task3,task4])