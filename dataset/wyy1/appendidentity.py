with open("identity.jsonl", "r", encoding="utf8") as fin:
    identity_lines = fin.readlines() 

with open("datafinal.jsonl", "a", encoding="utf8") as fout:
    for _ in range(50):
        fout.writelines(identity_lines) 

    