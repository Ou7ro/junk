import openpyxl as xl
from random import randint
from dict import very_bad_malfunction
from dict import malfunction


def get_value(model):
    values = f'{malfunction[model][randint(0, 3)]}, {very_bad_malfunction[randint(0, 3)]}'
    return values


def added_reasons(sheet, max_row):
    for i in range(2, max_row + 1):
        model = sheet.cell(row=i, column=1).value
        if model in malfunction:
            values = get_value(model)
            sheet.cell(column=3, row=i, value=values)
        else:
            sheet.cell(column=3, row=i, value='Неустранимые загрязнения')


def main():
    file_path = input('Введите название файла или же путь до него: ')
    if file_path is None:
        wb = xl.load_workbook('Утиль.xlsx', data_only=True)
    else:
        wb = xl.load_workbook(file_path, data_only=True)
    sheet = wb.active
    max_row = sheet.max_row
    added_reasons(sheet, max_row)
    if file_path is None:
        wb.save('Утиль.xlsx')
    else:
        wb.save(file_path)
    wb.close()

    print('Готово')


if __name__ == '__main__':
    main()
