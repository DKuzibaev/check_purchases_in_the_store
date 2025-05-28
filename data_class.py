import time

def check_time_spent(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"[{func.__name__}] Время выполнения: {elapsed:.2f} сек")
        return result
    return wrapper

class Data:
    def __init__(self, initial_data=None):
        self._data = initial_data if initial_data else []
        self._buffer = []
        self._data_base = []

    @check_time_spent
    def load_data(self, records):
        if not isinstance(records, list):
            raise TypeError("Ожидается список записей")
        self._buffer.extend(records)

    @property
    def all_data(self):
        return self._data + self._buffer

    @check_time_spent
    def send_data_base(self):
        # В реальном варианте здесь будет отправка в БД
        self._data_base.extend(self.all_data)
        print("Данные отправлены в базу")

    def get_data_base(self):
        return self._data_base
