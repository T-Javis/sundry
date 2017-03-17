import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

text_from_file_with_apath = open('/Users/hecom/23tips.txt').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud().generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()


'''
1～3 行分别导入了画图的库，词云生成库和jieba的分词库；

4 行是读取本地的文件,代码中使用的文本是本公众号中的《老曹眼中研发管理二三事》。

5～6 行使用jieba进行分词，并对分词的结果以空格隔开；

7行对分词后的文本生成词云；

8～10行用pyplot展示词云图。
'''