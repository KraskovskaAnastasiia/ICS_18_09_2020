
from dataclasses import dataclass

@dataclass
class Type:
    code: int
    type: str

@dataclass
class Enterprise:
    name: str
    code: int
    remainder: float
    received: float
    output: float

type_array = []
type_array.append(Type(1, "Будівлі"))
type_array.append(Type(2, "Машини та обладнання"))
type_array.append(Type(3, "Транспортні засобі"))
type_array.append(Type(4, "Інструмент та інвертар"))

enterprises_array = []
enterprises_array.append(Enterprise("Універсам 22", 1, 44048.00, 500.00, 200.00))
enterprises_array.append(Enterprise("Дніпрянка", 1, 22456.00, 365.00, 123.00))
enterprises_array.append(Enterprise("Універсам 22", 2, 5564.00, 2571.00, 135.00))
enterprises_array.append(Enterprise("Дніпрянка", 2, 10087.00, 15972.00, 58.00))
enterprises_array.append(Enterprise("Універсам 22", 3, 0.00, 0.00, 0.00))
enterprises_array.append(Enterprise("Дніпрянка", 3, 206.00, 34.00, 50.00))
enterprises_array.append(Enterprise("Універсам 22", 4, 116.00, 64.00, 23.00))
enterprises_array.append(Enterprise("Дніпрянка", 4, 34.00, 23.00, 25.00))

def printEnterprise(enterprise):
    '''printEnterprise function prints
    "Рух основних засобів"
    with names and values'''

    print("Назва: {name}, Код: {code}, Залишок,грн.: {remainder}, Надійшло,грн.: {received} Вибуток, грн.: {output}"
          .format(name=enterprise.name, code=enterprise.code, remainder=enterprise.remainder,
                  received=enterprise.received, output=enterprise.output))

for data in enterprises_array:
    printEnterprise(data)

def printType(type):
    '''printType function prints
    "Вид основних засобів"
    with names and values'''

    print("Код: {code}, Тип: {type}"
          .format(code=type.code, type=type.type))

for data in type_array:
    printType(data)
