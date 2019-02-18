# -*- coding: utf-8 -*-
import json
import time
import random
import requests


def filter_data(resp_data):
    data_dict = {'Hypernym': [], 'Hyponymy': []}
    class_data = resp_data['Classes']
    for dic in class_data:
        if dic.get('Hypernym'):
            for k in dic.get('Hypernym'):
                data_dict['Hypernym'].append(k['Label'])
        if dic.get('Hyponymy'):
            for j in dic.get('Hyponymy'):
                data_dict['Hyponymy'].append(j['Label'])
    return data_dict


url = 'http://api.xlore.org/query'
f = open('pick_dic.txt', encoding='utf-8')
result_ = {}
f_out = open('pick_dic.json','w+',encoding='utf-8')
line = f.readline()
while (line):
    try:
        print(line)
        line = line.strip('\n')
        line = line.replace('\ufeff','')
        payload = {'classes': line}
        print(random.random()+random.random()*random.random())
        time.sleep(random.random()+random.random()*random.random())
        resp = requests.get(url=url, params=payload)
        resp_data = resp.json()
        result = filter_data(resp_data)
        if line not in result_ and len(result['Hypernym']) > 0 and len(result['Hyponymy']) > 0:
            result_[line] = result
        # print(resp_data)
        line = f.readline()
    except Exception as e:
        mdata2 = json.dumps(result_, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
        f_out.writelines(mdata2)
        f_out.close()
mdata2 = json.dumps(result_, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
f_out.writelines(mdata2)
f_out.close()
