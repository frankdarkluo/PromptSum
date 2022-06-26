import json
from tqdm import tqdm

def preprocess(prefix):
    datas=json.loads(open(prefix+'.json','r',encoding='utf8').read())
    with open(prefix+'.jsonl','w',encoding='utf8') as of:
        for data in datas:
            data['dialogue']=data['dialogue'].replace('\r','').replace(' \r','')
            json.dump(data, of)
            of.write('\n')


preprocess('train')
preprocess('val')
preprocess('test')

