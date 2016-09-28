
t = []
dct = {}

def load_data(filepath):
    f = open('t.txt', 'r').read().lower().replace(',', '').replace('.', '').split(' ')
    for item in f:
    	t.append(item)
    return t
    f.close()
def get_most_frequent_words(text):
    for item in text:
    	if item in dct:
    		dct[item] += 1
    	else:
    		dct[item] = 1  
    return dct

if __name__ == '__main__':
	text = load_data('t.txt')
	d = get_most_frequent_words(text)
	l = lambda x: x[1]
	d = sorted(d.items(), key=l, reverse=True)
	for item in d[0:9]:
		print item[0], item[1]