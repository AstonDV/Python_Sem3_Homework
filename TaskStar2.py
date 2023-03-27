# *****(4)Напишите функцию, которая принимает словарь с параметрами и возвращает строку запроса,
# сформированную из отсортированных в лексикографическом порядке параметров.
# Пример:
# Код print(query({'course': 'python', 'lesson': 2, 'challenge': 17})) должен возвращать строку:
# challenge=17&course=python&lesson=2

def query(dictionary: dict) -> str:
    list = []
    for key, value in dictionary.items():
        list.append(f'{str(key)}={str(value)}')
    list.sort()
    text = ''
    for word in list[:-1]:
        text += word + '&'
    return text + str(list[-1])

print(query({'course': 'python', 'lesson': 2, 'challenge': 17}))
