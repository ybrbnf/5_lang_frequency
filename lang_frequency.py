import re
from collections import Counter


def load_data(filepath):
    return file_.read().lower()


def get_most_frequent_words(text):
    prepared_text = re.findall(r'\w+', text)
    counter = Counter(prepared_text)
    top_ten = 10
    return counter.most_common(top_ten)

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
