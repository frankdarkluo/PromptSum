import json
from tqdm import tqdm

def preprocess(prefix):
    datas=json.loads(open(prefix+'.json','r',encoding='utf8').read())
    with open(prefix+'.jsonl','w',encoding='utf8') as of:
        data_dict={'id':[],'dialogue':[],'summary':[]}
        for id,data in enumerate(datas):
            data_dict['id']=id
            data_dict['dialogue']=data[1]
            data_dict['summary']=data[0]
            json.dump(data_dict.copy(), of)
            of.write('\n')



preprocess('train')
preprocess('val')
preprocess('test')

