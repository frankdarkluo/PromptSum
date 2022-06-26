import json
TEST_SUMMARY_ID = 1

data = open('dialogsum.test.jsonl', "r").readlines()
result = {"fname": [], "summary%d" % TEST_SUMMARY_ID: [], "dialogue": []}
for i in data:
    d = json.loads(i)
    for j in d.keys():
        if j in result.keys():
            result[j].append(d[j])

result["summary"] = result["summary%d" % TEST_SUMMARY_ID]

with open('golden.txt','w',encoding='utf8') as of:
    for summary in result['summary']:
        of.write(summary+'\n')