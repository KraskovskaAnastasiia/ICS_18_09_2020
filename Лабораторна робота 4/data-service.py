
from dataclasses import dataclass

@dataclass
class TypeOfMainAssets:
    code: int
    type: str

@dataclass
class MoveOfMainAssets:
    name: str
    code: int
    remainder: float
    received: float
    output: float

type_array = []
type_array.append(TypeOfMainAssets(1, "Будівлі"))
type_array.append(TypeOfMainAssets(2, "Машини та обладнання"))
type_array.append(TypeOfMainAssets(3, "Транспортні засобі"))
type_array.append(TypeOfMainAssets(4, "Інструмент та інвертар"))

move_array = []
move_array.append(MoveOfMainAssets("Універсам 22", 1, 44048.00, 500.00, 200.00))
move_array.append(MoveOfMainAssets("Дніпрянка", 1, 22456.00, 365.00, 123.00))
move_array.append(MoveOfMainAssets("Універсам 22", 2, 5564.00, 2571.00, 135.00))
move_array.append(MoveOfMainAssets("Дніпрянка", 2, 10087.00, 15972.00, 58.00))
move_array.append(MoveOfMainAssets("Універсам 22", 3, 0.00, 0.00, 0.00))
move_array.append(MoveOfMainAssets("Дніпрянка", 3, 206.00, 34.00, 50.00))
move_array.append(MoveOfMainAssets("Універсам 22", 4, 116.00, 64.00, 23.00))
move_array.append(MoveOfMainAssets("Дніпрянка", 4, 34.00, 23.00, 25.00))

def printMoveOfMainAssets(moveOfMainAssets):
    '''printMoveOfMainAssets function prints
    "Рух основних засобів"
    with names and values'''

    print("Назва: {name}, Код: {code}, Залишок,грн.: {remainder}, Надійшло,грн.: {received} Вибуток, грн.: {output}"
          .format(name=moveOfMainAssets.name, code=moveOfMainAssets.code, remainder=moveOfMainAssets.remainder,
                  received=moveOfMainAssets.received, output=moveOfMainAssets.output))

for data in move_array:
    printMoveOfMainAssets(data)

def printTypeOfMainAssets(typeOfMainAssets):
    '''printTypeOfMainAssets function prints
    "Вид основних засобів"
    with names and values'''

    print("Код: {code}, Тип: {type}"
          .format(code=typeOfMainAssets.code, type=typeOfMainAssets.type))

for data in type_array:
    printTypeOfMainAssets(data)
