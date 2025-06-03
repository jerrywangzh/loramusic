import json

stylelist = set()

with open("dataset2.jsonl","r",encoding="utf8") as fin,open("style.jsonl","w",encoding="utf8") as fout:
    for i in fin:
        s = set(json.loads(i)["labels"].split())
        stylelist |= s
    fout.write(json.dumps(list(stylelist),ensure_ascii=False)+"\n")
    

    
        
