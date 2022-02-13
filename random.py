nums = ['{:04b}'.format(i).translate({ord("0"): ord("O"), ord("1"): ord("I")}) for i in range(16)]

print(nums)

# 0 to 7
nums_positive = ['{:04b}'.format(i).translate({ord("0"): ord("O"), ord("1"): ord("I")}) for i in range(0, 8)]

print(','.join(nums_positive))

nums_negative1 = ['{:04b}'.format(i).translate({ord("0"): ord("O"), ord("1"): ord("I")}) for i in range(0, 8)]
print(nums_negative1)

# -1 to -8
nums_negative = ', '.join(map(str, nums_negative1))

d = {"I": "O", "O": "I"}
t = str.maketrans(d)
f = nums_negative.translate(t)

print(nums_negative)
print('~~~~~~~~~~')
print(f)

# вывести весь «циферблат» от int4[-8] до int4[7]
print()
nums_positive = ', '.join(map(str, nums_positive))
bin_dial = f + ',' + nums_positive
print(bin_dial)

# напишите функцию инверсии inv4 которая строку из четырёх букв меняет I на O и наоборот. То есть например  “OIIO” в “IOOI”

def inv4(x: int) -> str:
    inv = str(f'{(x):04b}').translate({ord("0"): ord("O"), ord("1"): ord("I")})
    print(inv)

inv4(71)


def inv_str(x: str) -> str:
    d = {"I": "O", "O": "I"}
    t = str.maketrans(d)
    inv = x.translate(t)
    print(inv)

inv_str('IOOI')


"""исходя из п. 8 составить словарь minus_index  
где ключи от 0 до 7 переводятся в те же значения 
от от 0 до 7 а вот от ключи от 8 до 15 значения 
от -8 до -1 соответственно {0:0, 1:1,..., 7:7, 8:-8,9:-7,...,15:-1} 
Это соответствие  циферблатов положительных с циферблатом где есть оба знака (- и +)"""
# positive_part = {x: x for x in range(8)}
# print(positive_part)
# negative_keys = [i for i in range(8, 16)]
# negative_values = [i for i in range(-8, 0)]
# negative_part = zip(negative_keys, negative_values)
# minus_index = dict(zip(positive_part, negative_part))
# print(minus_index)

minus_index = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: -8, 9: -7, 10: -6, 11: -5, 12: -4, 13: -3, 14: -2, 15: -1}
int4 = ['{:04b}'.format(i).translate({ord("0"): ord("O"), ord("1"): ord("I")}) for i in range(16)]
all4 = {int4[i]: minus_index[int4.index(int4[i])] for i in range(len(minus_index))}
print(all4)


"""text = "Объекты bytearray являются изменяемыми." 
Создать из него bytearray. 
Заменить два первых байта на один байт b'\x4f' . 
А последний байт на нулевой байт. Декодировать обратно в текст. Что поменялось?"""











########
text = bytearray('Объекты bytearray являются изменяемыми', encoding='utf-8')
prin t(text[0:2], text[-1] = b'\x4f', 0)

text[0:2], text[-1] = b'\x4f', 0

b = 183 #'{:08b}'.format(183)

print(b:=int(b) >> 2)

print(b:=int(b) << 4)

mask = 0b11111111

print(b8 :=b & mask)

# rus_eng = ''.maketrans()

_line_ = 'Привет!'

def rus_to_eng_value(line:str) -> str:

    line.lower()

    rus_eng = {1072: 97, 1073: 98, 1094: 99, 1076: 100, 1077: 101, 1092: 102, 1075: 103, 1093: 104, 1080: 105,
               1078: 106, 1082: 107, 1083: 108, 1084: 109, 1085: 110, 1086: 111, 1087: 112, 1088: 114, 1089: 115,
               1090: 116, 1102: 117, 1074: 118, 1081: 121, 1079: 122}

    return line.translate(rus_eng)

# print(rus_to_eng_value(_line_))

_line_ = list(_line_)

def rus_to_eng_link(line:list) -> None:

    for i in range(len(line)):
            line[i] = line[i].lower()

            rus_eng = {1072: 97, 1073: 98, 1094: 99, 1076: 100, 1077: 101, 1092: 102, 1075: 103, 1093: 104, 1080: 105,
                       1078: 106, 1082: 107, 1083: 108, 1084: 109, 1085: 110, 1086: 111, 1087: 112, 1088: 114, 1089: 115,
                       1090: 116, 1102: 117, 1074: 118, 1081: 121, 1079: 122}

            line[i] = line[i].translate(rus_eng)


# print(rus_to_eng_value(line))

rus_to_eng_link((_line_))

print(''.join(_line_))

int4_values = {val:e for e,val in enumerate(int4)}

def adding_int4(value1:str, value2:str) -> str:
    int4_values = {val: e for e, val in enumerate(int4)}
    int4_answears = {e:val  for e, val in enumerate(int4)}
    sum = int4_values[value1] + int4_values[value2]
    return int4_answears[sum]


def substraction_int4(value1:str, value2:str) -> str:
    int4_values = {val: e for e, val in enumerate(int4)}
    int4_answers = {e:val  for e, val in enumerate(int4)}
    subs = int4_values[value1] - int4_values[value2]
    return int4_answers[subs]


print(adding_int4('IOII', 'IIOO'))

print(substraction_int4('IIOO','OOII'))

def medical_card_update(text:str, card:str=None) -> None:
    if card == None: card = '{}.txt'.format(input('Type new card name: '))
    with open(f'{card}.txt', 'a') as card:
        card.writelines('{}\n'.format(text))

medical_card_update('Hi, my name is Nik!', 'Nik_card2')