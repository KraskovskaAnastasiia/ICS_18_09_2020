#Імпортуємо модуль XlsxWriter за допомогою якого ми будемо записувати через Пітон файл дані у Ексель файл
import xlsxwriter

#Створюємо файл та даємо йому назву
workbook = xlsxwriter.Workbook('Excel_tablitsa2.xlsx')

#Створюємо лист (sheet) у нашій таблиці, нам знадобився всього лише один
worksheet = workbook.add_worksheet()

#Формат жирності текста
bold = workbook.add_format({'bold': True})

worksheet.write('A1', 'Код', bold)
worksheet.write('B1', 'Вид основних засобів', bold)

bold.set_align('center')


# У цей масив ми записуємо наші дані рядками, так як вони повинні розташовуватись у Ексель файлі
types = (
    ['1', 'Будівлі'],
    ['2', 'Машини та обладнання'],
    ['3', 'Транспортні засоби'],
    ['4', 'Інструмент та інвентар'],
)

worksheet.set_column(0, 2, 20)

#Вказуємо, з якої клітинки починається наша табличка
for i, (code, type) in enumerate (types, start=2):
    worksheet.write(f'A{i}', code)
    worksheet.write(f'B{i}', type)

# зберігаємо у папці проекту та закриваємо наш файл
workbook.close()