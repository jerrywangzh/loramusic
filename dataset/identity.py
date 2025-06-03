import json

wname1 = "Jingyao Gong"

name1 = "WangFeiYu,WangZheng,HuangJianLe,LiSongZe"

name2 = "王飞豫、王峥、黄键乐、李松泽"

with open("lora_identity (3).jsonl","r",encoding="utf8") as fin,open("identity.jsonl","w",encoding="utf8") as fout:
    for l in fin:
        d = json.loads(l)
        if wname1 in d["conversations"][1]["content"]:
            d["conversations"][1]["content"] = d["conversations"][1]["content"].replace(wname1,name1)
        fout.write(json.dumps(d,ensure_ascii=False)+"\n")
        