# Случайное присваивание неисправности терминалам.

Скрипт принимает файл 'Утиль.xlsx'(Пример есть в репозитории).
И возвращает этот же файл, но с уже прописанными неисправностями.
Также в файле с названием 'dict.py' находится список терминалов и их возможные неисправности.
Если в вашей бд хранится другео название терминала, можете смело изменить название в словаре.

Совместим с такими терминалами как:
- PAX_S90_GPRS_C_CTLS
- PAX_S80_EG_C_CTLS
- PAX_D230_4G_BT_WIFI_CTLS
- Ingenico_ICT220_EG_BW_CTLS
- VeriFone_PP1000SE_BW_CTLS
- Ingenico_ICT250_EG_C_CTLS
- Ingenico_IPP220_BW_CTLS
- Ingenico_IPP320_BW_CTLS
- Ingenico_IPP320_BW_CTLS
- PAX_S200_C_CTLS
- PAX_SP30_C_CTLS
- PAX_S300_C_CTLS
- Tactilion_G3_3G_C_CTLS
- Tactilion_T2_EG_C_CTLS
- 7.2
- EVOTOR_5_СТ5Ф
- VeriFone_Vx520_ED_BW_CTLS
- VeriFone_Vx820_C_CTLS
- Castles_VEGA3000_3G_C_CTLS

## Зависимости

- Python3.12* должен быть уже установлен
- Затем используйте `pip` для установки зависимостей:
```
pip install -r requirements.txt
```
##Xlsx файл.

Пример того, как должен быть заполнен файл.
![image](https://github.com/user-attachments/assets/d46ce023-4b5d-4cb3-b6dc-a1866c69db13)

1. Первая колонка должна быть занята названиями моделей терминалов. Для коректной работы, используйте названия из описания выше, либо с файла dict.py. Если же модели нет в этом файле, ему по умолчанию будет присваиваться значение 'Неустранимое загрязнение'.
2. Вторая колонка может быть заполнена серийными номерами. Но это не обязательное условие, на работу программы это не повлияет.
3. 


## Запуск

- Для добавления неисправностей:
```pycon
python main.py 
```

##Выходные данные

В консоли будет надпись `готово`.

Файл в корневой директории 'Утиль.xlsx' измениться.

Пример:

![image](https://github.com/user-attachments/assets/4f221c39-d430-4d68-9c38-32dd8f8e8460)
