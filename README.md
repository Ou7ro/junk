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

### Зависимости

- Python3 должен быть уже установлен
- Затем используйте `pip` для установки зависимостей:
```pycon
pip install -r requirements.txt
```

## Запуск

- Для добавления неисправностей:
```pycon
python main.py 
```

