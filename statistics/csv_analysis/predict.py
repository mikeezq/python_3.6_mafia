import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Загрузка датасета
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv(r'C:\Users\germa\Downloads\Telegram Desktop\participants_merged.csv')
df = pd.get_dummies(df, columns=['replaced_delivery_region'])
# Удаление текстовых полей и преобразование даты в числовой формат
df.drop(['id', 'supplier_inn', 'is_winner', 'code_label', 'publish_price',
         'delivery_region', 'preprocessed_code', 'code', 'code_name',
         'contract_reg_number', 'publish_date'], axis=1, inplace=True)
df['contract_conclusion_date'] = pd.to_datetime(df['contract_conclusion_date'])
df['contract_conclusion_date_numb'] = df['contract_conclusion_date'].astype(np.int64) // 10 ** 9
# Разделение на тренировочную и тестовую выборки
X = df.drop('end_price', axis=1)
y = df['end_price']

for i in range(1, 4):
    X[f'tender_price_lag_{i}'] = y.shift(i)

# Удаление строк с пропущенными значениями
X.dropna(inplace=True)
y = y[X.index]
# Разделение на обучающий и тестовый наборы данных
X_train = X[X['contract_conclusion_date'] < pd.to_datetime('2021-03-01', format='%Y-%m-%d')]
X_test = X[X['contract_conclusion_date'] >= pd.to_datetime('2021-03-01', format='%Y-%m-%d')]
y_train = y[X_train.index]
y_test = y[X_test.index]
y_train = y[X['contract_conclusion_date'] < pd.to_datetime('2021-03-01', format='%Y-%m-%d')]
y_test = y[X['contract_conclusion_date'] >= pd.to_datetime('2021-03-01', format='%Y-%m-%d')]
X_train.drop('contract_conclusion_date', axis=1, inplace=True)
X_test.drop('contract_conclusion_date',  axis=1, inplace=True)


# Создание дополнительных признаков на основе гармоник Фурье
def create_fourier_features(X, n_harm):
    n_samples, n_features = X.shape
    t = np.arange(n_samples)
    X_new = np.zeros((n_samples, n_features + 2*n_harm))
    X_new[:,:n_features] = X
    for i in range(n_harm):
        X_new[:,n_features+i] = np.sin(2*np.pi*(i+1)*t/n_samples)
        X_new[:,n_features+n_harm+i] = np.cos(2*np.pi*(i+1)*t/n_samples)
    return X_new

# Количество гармоник Фурье, которые мы хотим использовать
n_harm = 3

# Создание дополнительных признаков на основе гармоник Фурье
X_train_fourier = create_fourier_features(X_train, n_harm)
X_test_fourier = create_fourier_features(X_test, n_harm)
print(2, X_train.shape)
# Создание и обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train_fourier, y_train)
print(3, X_train.shape)
# Предсказание на тестовых данныхq
y_pred = model.predict(X_test_fourier)

# Оценка точности модели
score = model.score(X_test_fourier, y_test)


# Оценка точности модели
print("R^2 score:", score)

plt.figure(figsize=(10, 6))
plt.plot(y_test.values, label='True values')
plt.plot(y_pred, label='Predicted values')
plt.legend()
plt.xlabel('Sample index')
plt.ylabel('End price')
plt.show()

errors = np.abs(y_pred - y_test.values)
plt.figure(figsize=(10, 6))
plt.hist(errors, bins=50)
plt.xlabel('Absolute error')
plt.ylabel('Frequency')
plt.show()

