# Pandas

[**1. Как создавать, читать и записывать данные**](https://github.com/devFF/FindJob/blob/main/Data_processing/Pandas/creating_reading_writing.py) с помощью библиотеки Pandas.
Здесь рассматриваются основные объекты Pandas: DataFrame (table) и Series (list).
Индексы DataFrame и Series могут быть записаны в любой форме, [example](https://github.com/devFF/FindJob/blob/5c11650e2b0bddc0514ade168bf0a8196426feec/Data_processing/Pandas/creating_reading_writing.py#L18).
 
[**2. Определение типов данных и пропущенных значений**](https://github.com/devFF/FindJob/blob/main/Data_processing/Pandas/data_types_and_missing_values.py).

Вывод типа данных для каждой колонки [**.dtypes**](https://github.com/devFF/FindJob/blob/47a8eab8304c3277869630808ad2213416af0606/Data_processing/Pandas/data_types_and_missing_values.py#L12) 
или для отдельной колонки [**.dtype**](https://github.com/devFF/FindJob/blob/47a8eab8304c3277869630808ad2213416af0606/Data_processing/Pandas/data_types_and_missing_values.py#L13). 

Преобразование типа данных методом [**.astype('int64')**](https://github.com/devFF/FindJob/blob/47a8eab8304c3277869630808ad2213416af0606/Data_processing/Pandas/data_types_and_missing_values.py#L14).

Поиск пропущенных значений в колонке (column) при помощи метода [**.isnull(column)**](https://github.com/devFF/FindJob/blob/47a8eab8304c3277869630808ad2213416af0606/Data_processing/Pandas/data_types_and_missing_values.py#L18).

Замена пропущенных значений на выбранное [**.fillna('new_value')**](https://github.com/devFF/FindJob/blob/47a8eab8304c3277869630808ad2213416af0606/Data_processing/Pandas/data_types_and_missing_values.py#L19). \n

Замена не пропущенных значений **.replace('was','became')**.


