import openpyxl as xl
from random import randint
from dict import malfunction


def get_value(model):
    value = f'{malfunction[model][randint(0, 3)]}, {malfunction[model][randint(4, 7)]}'
    return value


def added_reasons(sheet, max_row):
    for i in range(2, max_row + 1):
        model = sheet.cell(row=i, column=1).value
        if model in malfunction:
            value = get_value(model)
            sheet.cell(column=3, row=i, value=value)
        else:
            sheet.cell(column=3, row=i, value='Неустранимые загрязнения')


wb = xl.load_workbook('Утиль.xlsx', data_only=True)
sheet = wb.active
max_row = sheet.max_row
added_reasons(sheet, max_row)
wb.save('Утиль.xlsx')
wb.close()

print('Готово')
