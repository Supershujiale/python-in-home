#CalHamletV1.py
def getText():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~‘’':
        txt = txt.replace(ch,"")
    return txt

hamletText = getText()
words = hamletText.split()#以空格为分隔符 将每个单词变成列表words中的一个单独字符串
counts = {}
for word in words:
    counts[word] = counts.get(word,0) +1
items = list(counts.items())
items.sort(key=lambda  x:x[1],reverse=True)#根据键值对的第二个元素进行由大到小的排序
for i in range(10):
    word,count = items[i]
    print('{0:<10}{1:>5}'.format(word,count))#0和1用来指定位置