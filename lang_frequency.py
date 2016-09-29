import re


def load_data(filepath):
    lst = []
    try:
        with open(filepath, 'r') as file_:
            txt = file_.read()
            txt = re.sub(u'[^а-яА-Яa-zA-Z\s\w]', '', txt)
            txt = re.sub(r'[\n*]', ' ', txt)
            txt = re.split(' ', txt)
            for item in txt:
                lst.append(item)
        return lst
    except FileNotFoundError:
        print ('Нет такого файла или папки. Программа будет закрыта.')
        exit()
    


def get_most_frequent_words(text):
    dct = {}
    for item in text:
        if item in dct:
            dct[item] += 1
        else:
            dct[item] = 1
    dct = sorted(dct.items(), key=lambda x: x[1], reverse=True)
    return dct

if __name__ == '__main__':
    filepath = input('Вседите путь и имя файла: ')
    text = load_data(filepath)
    d = get_most_frequent_words(text)
    for item in d[0:9]:
        print (item[0], item[1])
