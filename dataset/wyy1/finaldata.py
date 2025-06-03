import json

from format import greeting,question,answer

from random import sample,choice






with open("dataset2.jsonl","r",encoding="utf8") as f:
    fin = f.readlines()

with open("style.jsonl","r",encoding="utf8") as style:
    styles = json.load(style)


style2 = ["欧美","流行", "网络歌曲","古风", "华语", "电子"]

with open("datafinal.jsonl","w",encoding="utf8") as fout:
    for j in range(200):
        s = choice(style2)
        num = 0
        for i in fin:
            i = json.loads(i)
            if s in i["labels"]:
                num += 1
                singer = "、".join(i["names"])
                otherstyle = "、".join([j for j in i["labels"].split()])
                name = i["song"]
                description = i["description"]
                for m in range(3):
                    fout.write(json.dumps(
                        {
                            "conversations":[
                                {
                                    "role":"user",
                                    "content":f"{question(s)}"
                                },
                                {
                                    "role":"assistant",
                                    "content":f"{answer(name,singer,otherstyle,description)}"
                                }
                            ]
                        },ensure_ascii=False
                    )+"\n")
            if num == 50:
                break