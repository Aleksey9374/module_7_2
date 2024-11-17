# Задача "Записать и запомнить":
# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи,
# strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
# а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell()
# перед записью.
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file: #Открываем файл ч/з конструкцию with которая закрывает файл
        # после закрытия блока
        for i,string in enumerate(strings, start=1): #Пробегаемся по элементам списка с присвоением индексов начиная с 1
            byte = file.tell() #Tекущая позиция указателя чтения/записи в файле в байтах
            file.write(string + '\n') #Записываем полученные строки по переданным в strings значениям info
            strings_positions[(i, byte)] = string #Собираем полученные значения в словарь
        return strings_positions #Результатом возвращаем словарь по всем значениям

result = custom_write('test.txt', info)
for elem in result.items(): #Выводим на печать список кортежей полученного словаря
  print(elem)
