dist_path = './dist/'
index_file = 'index.html'

text = open(dist_path + index_file, 'r', encoding='utf8').read()

text = text.replace('/js/', '/dist/js/')
text = text.replace('/css/', '/dist/css/')

with open(dist_path + index_file, 'w', encoding='utf8') as f:
    f.write(text)