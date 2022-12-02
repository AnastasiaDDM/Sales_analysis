import pandas as pd
import matplotlib.pyplot as plt

# Получение данных
data = pd.read_excel("content/contracts.xlsx")

# Настройки для отображения таблицы
# pd.set_option('max_rows', None)
# pd.set_option('max_columns', None)
# pd.set_option('display.max_colwidth', None)
# pd.set_option('display.float_format', '{:.2f}'.format)


# Сортировка по 'Товар', 'Город'
print("\nСортировка по 'Товар', 'Город' ")
print(data.sort_values(by=['Товар', 'Город']))


# Сортировка по 'Товар', 'Продавец', 'Единица измерения'
print("\nСортировка по 'Товар', 'Продавец', 'Единица измерения' ")
print(data.sort_values(by=['Товар', 'Продавец', 'Единица измерения']))


# Количество проданных товаров по городам
print("\nКоличество проданных товаров по городам ")
print(data.groupby(['Город'])["Количество"].sum())
# График для наглядного представления
(data.groupby(['Город'])["Количество"].sum()).plot(kind="bar", title= 'Количество проданных товаров по городам')
plt.show()


# Первые 10 максимальных по стоимости продаж
print("\nПервые 10 максимальных по стоимости продаж ")
data['Стоимость'] = data['Цена']*data['Количество']
print(data.sort_values('Стоимость', ascending=False).head(10))


#  Продажи, финансируемые банками "Богатырский" или "Надежный"
print("\nПродажи, финансируемые банками 'Богатырский' или 'Надежный' ")
filter_0 = (data['Банк'] == 'Богатырский') | (data['Банк'] == 'Надежный')
print(data[filter_0])


# Общее количество проданных круп в городе Иркутске
filter_1 = (data['Группа товаров'] == 'Крупы') & (data['Город'] == 'Иркутск')
print("\nОбщее количество проданных круп в городе Иркутске = %d мешков"  %(data[filter_1]['Количество'].sum()))
new_data = (data[filter_1].groupby(['Товар'])).sum()
print(new_data['Количество'])

# Круговая диаграмма
fig1, ax1 = plt.subplots()
wedges, texts, autotexts = ax1.pie(new_data['Количество'], labels=new_data.axes[0], autopct='%1.2f%%')
ax1.axis('equal')
plt.show()

# Сумма продаж, осуществлённых организацией "Единство"
filter_2 = (data['Продавец'] == 'Единство')
print("\nСумма продаж, осуществлённых организацией 'Единство' = %d продаж на общую стоимость %d руб. " %(len(data[filter_2]), data[filter_2]['Стоимость'].sum()))


# Количество продаж в разрезе наименования товара и фирмы
print("\nКоличество продаж в разрезе наименования товара и фирмы ")
print(data.groupby(['Товар', 'Продавец'])['Товар'].count())

# Настройки отображения для сводной таблицы
pd.set_option('max_rows', None)
pd.set_option('max_columns', None)
pd.set_option('display.max_colwidth', None)
print("\nСводная таблица: ")
print(data.pivot_table(index= 'Продавец' , columns='Товар', values= 'Количество' , aggfunc='count', fill_value=0))