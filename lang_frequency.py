import re
from collections import Counter


def load_data(filepath):
    txt = file_.read().lower()
    return txt


def get_most_frequent_words(text):
    txt = re.findall(r'\w+', text)
    counter = Counter(txt)
    top = 10
    txt = counter.most_common(top)
    return txt


if __name__ == '__main__':
    try:
        filepath = input('Вседите путь и имя файла: ')
        with open(filepath, 'r') as file_:
            text = load_data(filepath)
    except FileNotFoundError:
        print ('Нет такого файла или папки. Программа будет закрыта.')
        exit()
    top_ten_words = get_most_frequent_words(text)
    for item in top_ten_words:
        print (item[0], item[1])
