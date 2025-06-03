import json

from format2 import greeting,question,answer

from random import sample,choice



with open("dataset2.jsonl","r",encoding="utf8") as f:
    fin = f.readlines()

with open("style.jsonl","r",encoding="utf8") as style:
    styles = json.load(style)


style2 = ["欧美","流行", "轻音乐","古风", "华语", "电子","粤语"]


with open("datafinal.jsonl","w",encoding="utf8") as fout:
    for diedai in range(10):
        for index in range(6):
            s = style2[index]
            num = 0
            finalquestion = [""]*20
            finalanswer = [""]*20
            songnum = 0
            descriptiondict = dict()
            for i in fin:
                i = json.loads(i)
                if s in i["labels"]:
                    singer = "、".join(i["names"])
                    allstyle = "、".join([j for j in i["labels"].split()])
                    name = i["song"]
                    description = i["description"]
                    if finalquestion[0] == "":
                        finalanswer = [greeting() for i in finalanswer]
                        finalquestion = [i+question(s) for i in finalquestion]
                
                    if description not in descriptiondict:
                        finalanswer = [i+answer(name,singer,allstyle,description) for i in finalanswer]
                        descriptiondict[description]=1
                        num += 1
                    if num>4:
                        for fq,fa in zip(finalquestion,finalanswer):
                            fout.write(json.dumps(
                                {
                                    "conversations":[
                                        {
                                            "role":"user",
                                            "content":fq
                                        },
                                        {
                                            "role":"assistant",
                                            "content":fa
                                        }
                                    ]
                                },ensure_ascii=False
                            )+"\n")
                        num = 0
                        finalquestion = [""]*20
                        finalanswer = [""]*20

                

