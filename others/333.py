# -*- coding: utf-8 -*-
__author__ = 'Guanshanyou'

import jieba
import wordcloud

# 读取弹幕文件
def rand_file(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        dan_mu = f.read()
        return dan_mu


# 结巴分词 生成词云
def jieba_cut(str, imgname):
    cut_list = jieba.lcut(str)
    word = ' '.join(cut_list)
    w = wordcloud.WordCloud(font_path='msyh.ttf', background_color='white', width=600, height=400)
    w.generate(word)
    w.to_file(f'{imgname}.png')


if __name__ == '__main__':
    dvid = input('输入B站视频后缀：')
    str = rand_file(f'{dvid}.txt')
    jieba_cut(str, dvid)
    print('词云图生成完毕')