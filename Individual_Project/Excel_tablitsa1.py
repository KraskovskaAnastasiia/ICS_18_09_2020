#Імпортуємо модуль XlsxWriter за допомогою якого ми будемо записувати через Пітон файл дані у Ексель файл
import xlsxwriter

#Створюємо файл та даємо йому назву
workbook = xlsxwriter.Workbook('Excel_tablitsa1.xlsx')

#Створюємо лист (sheet) у нашій таблиці, нам знадобився всього лише один
worksheet = workbook.add_worksheet()

#Формат жирності текста
bold = workbook.add_format({'bold': True})

worksheet.write('A1', 'Підприємство', bold)
worksheet.write('B1', 'Код', bold)
worksheet.write('C1', 'Залишок на 1.01.2018', bold)
worksheet.write('D1', 'Надійшло у 2018', bold)
worksheet.write('E1', 'Вибуток у 2018', bold)

bold.set_align('center')

# У цей масив ми записуємо наші дані рядками, так як вони повинні розташовуватись у Ексель файлі
enterprise = (
    ['Універсам 22', '1', '44 048,00', '500,00', '200,00'],
    ['Дніпрянка   ', '1', '22 456,00', '365,00', '123,00'], 
    ['Універсам 22', '2', '5 564,00', '2 571,00', '135,00'],
    ['Дніпрянка   ', '2', '10 087,00', '15972,00', '58,00'],
    ['Універсам 22', '3', '0,00', '0,00', '0,00'],
    ['Дніпрянка   ', '3', '206,00', '34,00', '50,00'],
    ['Універсам 22', '4', '116,00', '64,00', '23,00'], 
    ['Дніпрянка   ', '4', '34,00', '23,00', '25,00'],
)

worksheet.set_column(0, 4, 20)

#Вказуємо, з якої клітинки починається наша табличка
for i, (name, code, remainder, received, output) in enumerate(enterprise, start=2):
    worksheet.write(f'A{i}', name)
    worksheet.write(f'B{i}', code)
    worksheet.write(f'C{i}', remainder)
    worksheet.write(f'D{i}', received)
    worksheet.write(f'E{i}', output)

# зберігаємо у папці проекту та закриваємо наш файл
workbook.close()