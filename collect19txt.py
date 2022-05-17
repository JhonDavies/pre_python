import jieba
txt = open("","r",encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word)== 1:
        continue
    else:
        rword = word
        counts[rword] = counts.get(rword,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))