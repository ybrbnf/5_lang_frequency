import re


def load_data(filepath):
    lst = []
    file_ = open(filepath, 'r').read().lower()
    text = re.sub(u'[^а-яА-Яa-zA-Z\s\w]', '', file_)
    text = re.sub(r'[\n*]', ' ', text)
    text = re.split(' ', text)
    for item in text:
        lst.append(item)
    return lst


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
