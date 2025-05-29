import clickhouse_connect
import main
import time

income_data = main

client = clickhouse_connect.get_client(
    host='localhost',
    port=8123,
    username='admin',
    password='secret',
    database='default'
)

client.command('''
CREATE TABLE IF NOT EXISTS report_data (
    metric String,
    value String
) ENGINE = MergeTree()
ORDER BY metric
''')

rows = [(d["metric"], d["value"]) for d in income_data.report_data]

client.insert('report_data', rows, column_names=['metric', 'value'])

def send_to_clickhouse(client, table_name, rows, column_names):
    start_time = time.time()  # время начала
    client.insert(table_name, rows, column_names=column_names)
    end_time = time.time()  # время окончания
    duration = round(end_time - start_time, 4)
    print(f"Данные отправлены в ClickHouse за {duration} секунд.")
    return duration

send_to_clickhouse(client, 'report_data', rows, column_names=['metric', 'value'])
