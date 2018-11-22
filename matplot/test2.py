import matplotlib.pyplot as plt     # 数学绘图库
import jieba               # 分词库
from wordcloud import WordCloud   #词云库

text = open('xyj.txt',"r").read()
cut_text= jieba.cut(text)
result= "/".join(cut_text)#必须给个符号分隔开分词结果来形成字符串,否则不能绘制词云


wc = WordCloud(font_path=r"simsun.ttf", background_color='white',width=800,height=600,max_font_size=200,
               max_words=10000,min_font_size=5,mode='RGBA')
wc.generate(result)
#wc.to_file("wordcloud.png") #按照设置的像素宽高度保存绘制好的词云图，比下面程序显示更清晰
plt.figure("词云图") #指定所绘图名称
plt.imshow(wc)       # 以图片的形式显示词云
plt.axis("off")      #关闭图像坐标系
plt.show()
