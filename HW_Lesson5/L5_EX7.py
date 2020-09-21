"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
данные о фирме. Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
"""

import json

with open("text_7.txt", "r", encoding='utf-8') as open_file:
    list_raw = open_file.readline().split()
    firm_dic = {}
    while list_raw:
        firm_dic[list_raw[0]] = int(list_raw[-2]) - int(list_raw[-1])
        list_raw = open_file.readline().split()
        fin_list = [i for i in firm_dic.values() if i > 0]
    average_dic = dict([("average_profit", sum(fin_list) / len(fin_list))])

with open("text_ex7.json", "w", encoding='utf-8') as open_json:
    json.dump([firm_dic, average_dic], open_json, ensure_ascii=False, indent=4)
