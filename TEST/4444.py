# -*- coding: utf-8 -*-
__author__ = 'Guanshanyou'

import requests
import json
import re


# 下载页面
def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    return res


# 根据dvid获取cid
def get_cid(dvid):
    '''
    获取cid
    :param dvid: https://api.bilibili.com/x/player/pagelist?bvid=BV1KK4y1h76a&jsonp=jsonp
    :return: cid
    '''
    url = f'https://api.bilibili.com/x/player/pagelist?bvid={dvid}&jsonp=jsonp'
    res = download_page(url)
    print(res)
    return json.loads(res.text)['data'][0]['cid']


# 根据cid请求弹幕
def get_msg(cid):
    '''
    :param cid: https://api.bilibili.com/x/v1/dm/list.so?oid=241955049
    :return:
    '''
    url = f'https://api.bilibili.com/x/v1/dm/list.so?oid={cid}'
    res = download_page(url)
    res.xml = res.content.decode('utf-8')
    patten = re.compile('<d.*?>(.*?)</d>')
    dan_mu_list = patten.findall(res.xml)
    return dan_mu_list


# 保存弹幕到txt文件
def save_to_file(dan_mu_list, filename):
    with open(filename, mode='w', encoding='utf-8') as f:
        for i in dan_mu_list:
            f.write(i)
            f.write('\n')


# 爬取弹幕主程序
def main(dvid):
    cid = get_cid(dvid)
    dan_mu_list = get_msg(cid)
    save_to_file(dan_mu_list, f'{dvid}.txt')


if __name__ == '__main__':
    # dvid = 'BV1aE411d7Rp'
    dvid = input('输入B站视频后缀：')
    main(dvid)
    print('弹幕爬取成功')
