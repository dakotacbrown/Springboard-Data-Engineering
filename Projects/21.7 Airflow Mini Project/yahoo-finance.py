from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd


def finance_download(stock):
    start_date = datetime.today()
    end_date = start_date + timedelta(days=1)
    start_date = start_date.strftime("%Y-%m-%d")
    end_date = end_date.strftime("%Y-%m-%d")
    df = yf.download(stock, start=start_date, end=end_date, interval='1m')
    df.to_csv(f'~/data/tmp/{datetime.today().strftime("%Y-%m-%d")}/{stock}/data.csv', header=False)


def query(stock1, stock2):
    df1 = pd.read_csv(f'~/data/{datetime.today().strftime("%Y-%m-%d")}/{stock1}/data.csv')
    df1.head()

    df2 = pd.read_csv(f'~/data/{datetime.today().strftime("%Y-%m-%d")}/{stock2}/data.csv')
    df2.head()


default_arguments = {
    'owner': 'Dakota',
    'email': 'dakotacbrown@gmail.com',
    'start_date': datetime(2022, 7, 13),
}


etl_dag = DAG(
    'market_vol',
    default_args=default_arguments,
    description='A simple finance DAG',
    schedule_interval=timedelta(days=1)
)



t0 = BashOperator(
    task_id='mk_tmp_dir',
    bash_command=f'\
        mkdir -p ~/data/tmp/{datetime.today().strftime("%Y-%m-%d")}/TSLA | \
        mkdir -p ~/data/tmp/{datetime.today().strftime("%Y-%m-%d")}/AAPL | \
        mkdir -p ~/data/{datetime.today().strftime("%Y-%m-%d")}/TSLA | \
        mkdir -p ~/data/{datetime.today().strftime("%Y-%m-%d")}/AAPL \
    ',
    dag=etl_dag
)


t1 = PythonOperator(
    task_id='download_AAPL',
    python_callable=finance_download,
    op_kwargs={'stock': 'AAPL'},
    dag=etl_dag
)


t2 = PythonOperator(
    task_id='download_TSLA',
    python_callable=finance_download,
    op_kwargs={'stock': 'TSLA'},
    dag=etl_dag
)


t3 = BashOperator(
    task_id='mv_AAPL',
    bash_command=f'mv ~/data/tmp/{datetime.today().strftime("%Y-%m-%d")}/AAPL/* ~/data/{datetime.today().strftime("%Y-%m-%d")}/AAPL',
    dag=etl_dag
)


t4 = BashOperator(
    task_id='mv_TSLA',
    bash_command=f'mv ~/data/tmp/{datetime.today().strftime("%Y-%m-%d")}/TSLA/* ~/data/{datetime.today().strftime("%Y-%m-%d")}/TSLA',
    dag=etl_dag
)


t5 = PythonOperator(
    task_id='run_query',
    python_callable=query,
    op_kwargs={
        'stock1': 'AAPL',
        'stock2': 'TSLA'
    },
    dag=etl_dag
)


t1 >> t3
t2 >> t4
t3 >> t5
t4 >> t5