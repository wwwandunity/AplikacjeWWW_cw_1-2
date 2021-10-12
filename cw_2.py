# Zadanie 1
def dwie_listy(a_list, b_list):
    new_list = []
    for x in range(len(a_list)):
        if x % 2 == 0:
            new_list.append(a_list[x])

    for x in range(len(b_list)):
        if x % 2 == 1:
            new_list.append(b_list[x])

    return new_list


print(dwie_listy([1,2,3,4], [5,6,7,8]))
# Zadanie 2


def slownik_z_tekstu(data_text):
    slownik = {
        "length": len(data_text),
        "letters": [x for x in data_text],
        "big_letters": data_text.upper(),
        "small_letters": data_text.lower()
    }

    return slownik


print(slownik_z_tekstu("siema"))
# Zadanie 3


def usun_litere(text, letter):
    return text.replace(letter, "")


print(usun_litere("czeresnie", "e"))


# Zadanie 4
def convert_temperature(number, temperature_type):
    if not isinstance(number, int) or isinstance(number, float):
        return "Wrong number type!"
    if temperature_type == "F":
        return number * 9 / 5 + 32
    if temperature_type == "K":
        return number + 273.15
    if temperature_type == "R":
        return number * 1.8 + 491.67

    return "Wrong temperature type!"


print(convert_temperature(5, "R"))


# Zadanie 5

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def difference(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b


print(Calculator.difference(5, 15))


# Zadanie 6
class ScienceCalculator(Calculator):
    @staticmethod
    def modulo(a, b):
        return a % b


print(ScienceCalculator.add(5, 15))
print(ScienceCalculator.modulo(6, 4))


# Zadanie 7
def od_tylu(text):
    return text[::-1]

print(od_tylu("mama"))


# Zadanie 8, 9
import file_manager

print(file_manager.FileManager("test.txt").read_file())
file_manager.FileManager("test.txt").update_file("dodawany_tekst")
print(file_manager.FileManager("test.txt").read_file())

# Zadanie 10
import chuck_norris


chuck_norris.chuck_norris("Mysz")