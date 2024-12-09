import urllib.request
from urllib.parse import quote #для преобразования в аский в строке запроса
import pandas as pd


russian_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" #руский алфавит
counter_by_letter = {key:0 for key in russian_alphabet} #создаем словарь на каждую букву
current_word = "Аардоникс" #начинаем с первого слова

while True: #идем пока не закончатся названия не на русском
    current_title = "title=\"" + current_word #создаем искомый тэг
    request_gen = urllib.request.urlopen("https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&from=" + quote(current_word)) #создаем запрос
    html_bunch = request_gen.read() #читаем его
    text = html_bunch.decode("utf8") #декодируем
    tags = text.split("\n") #делим на строки

    line_counter = 0

    while True: #в этом цикле мы идем по тегам, пока не начинаются названия
        if current_title in tags[line_counter]:
            break
        line_counter += 1
    
    for i in range(199): # а здесь уже идем букву и инкрисим соотвествующее значения в словаре
        for letter in tags[line_counter]:
            if letter in russian_alphabet:
                counter_by_letter[letter] += 1
                break
        line_counter += 1

    new_search = tags[line_counter-1]
    current_word = new_search[new_search.rfind("\">")+2:new_search.rfind("</a>")] #обновляем слово с которого показывается страничка. берем его с конца списка

    print(counter_by_letter) #выводим текщие значения дле дебага (я решил, что логировать в отедльный файл не имеет смысла в этом кейсы)
    print(current_word) 

    if current_word[0] not in russian_alphabet: #брейкаем, если русские названия закончились
        break


assert counter_by_letter["Й"] == 4 #Я страдал, но посчитал (хотя ближе к концу просто делал ctrl+f по html странице)
assert counter_by_letter["Е"] == 105
assert counter_by_letter["Ё"] == 2
assert counter_by_letter["Ш"] == 291
assert counter_by_letter["Ь"] == 0

#теперь перенесем в эксель

output_dt = pd.DataFrame(counter_by_letter.items(),columns=["Буква","Количество"])
print(output_dt)
output_dt.to_csv("output.xlsx", index = False)