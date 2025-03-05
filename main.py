import openpyxl as xl
from random import choices
from dict import malfunction


def get_value(model):
    value = choices(malfunction[model], k=2)
    values = f'{value[0]}, {value[1]}'
    return values


def added_reasons(sheet, max_row):
    for i in range(2, max_row + 1):
        model = sheet.cell(row=i, column=1).value
        if model in malfunction:
            values = get_value(model)
            sheet.cell(column=3, row=i, value=values)
        else:
            sheet.cell(column=3, row=i, value='Неустранимые загрязнения')


wb = xl.load_workbook('Утиль.xlsx', data_only=True)
sheet = wb.active
max_row = sheet.max_row
added_reasons(sheet, max_row)
wb.save('Утиль.xlsx')
wb.close()

print('Готово')
