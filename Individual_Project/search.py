from dataclasses import dataclass

@dataclass
class Enterprise:
    name: str
    code: int
    remainder: int
    received: int
    output: int


Enterprises_list = [
    Enterprise("Універсам 22", 1,  44048, 500, 200),
    Enterprise("Дніпрянка", 1,  22456, 365, 123),
    Enterprise("Універсам 22", 2,  5564, 2571, 135),
    Enterprise("Дніпрянка", 2, 10087, 15972, 58),
    Enterprise("Універсам 22", 3, 0, 0, 0),
    Enterprise("Дніпрянка", 3, 206, 34, 50),
    Enterprise("Універсам 22", 4, 116, 64, 23),
    Enterprise("Дніпрянка", 4, 34, 23, 25),
]


def print_enterprise(Enterprise):
    print("\nНазва: {name}\nКод: {code}\nЗалишок: {remainder}\nНадійшло: {received}\nВибуток: {output}".format(enterprise_name=Enterprise.enterprise_name,
                                                                                                                                   code=Enterprise.code, remainder=Enterprise.remainder, received=Enterprise.received, output=Enterprise.output))

class InfoEnt():

    def __init__(self):
        self.Enterprises = []

    def print_all_enterprises(self):
        for Enterprise in self.Enterprises:
            print_enterprise(Enterprise)

InfoEnt = InfoEnt()

InfoEnt.print_all_enterprises()