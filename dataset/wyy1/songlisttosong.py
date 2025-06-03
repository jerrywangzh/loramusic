import os
import json
import requests
import pandas as pd

# 1. 读入你的 CSV
df = pd.read_csv('MusicList.csv', encoding='utf-8')

# 2. 输出文件
out_path = 'dataset2.jsonl'
# 如果想每次重写，就去掉下面这行；想追加就改成 'a'
with open(out_path, 'w', encoding='utf-8') as fout:
    j = 1
    # 3. 遍历每个歌单
    for _, row in df.iterrows():
        style = row["Labels"]+"，描述为"+ row['SongListName']           # “风格”
        playlist_id = row['SongsListID']

        # 4. 请求歌单详情
        url_pl = f'http://localhost:3000/playlist/detail?id={playlist_id}'
        resp_pl = requests.get(url_pl)
        data_pl = resp_pl.json()
        track_ids = data_pl['playlist']['trackIds']

        # 5. 逐首取歌名和歌手
        i = 0
        for t in track_ids:
            song_id = t['id']
            url_s = f'http://localhost:3000/song/detail?ids={song_id}'
            resp_s = requests.get(url_s)
            data_s = resp_s.json()

            song = data_s['songs'][0]

            # ar 字段是一个列表，可能多个歌手
            names = [a['name'] for a in song['ar']]

            # 6. 构造一条记录（你也可以直接把列表 join 成字符串）
            record = {
                "role":"assistant",
                "content":f"歌曲作者是{"、".join(names)},作曲是{song['name']},本歌曲风格是{style}"
            }
            fout.write(json.dumps(record, ensure_ascii=False) + '\n')
        print("歌单数量：",j)
        j+=1
        print(f'写入歌单 "{style}" 成功 ')

