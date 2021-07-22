"""
Simple script to convert google keep default json exports to txt for importing in other note taking apps
"""

import simplejson as json
import os

file_list = os.listdir("/home/depsy/Deepanshu/Extra/keep/takeout-20210722T103201Z-001/Takeout/Keep")

for i,file in enumerate(file_list):
    f = open(f'/home/depsy/Deepanshu/Extra/keep/takeout-20210722T103201Z-001/Takeout/Keep/{file}',)
    data = json.load(f)
    yuh = open(f'{file}.txt','w')
    yuh.write(data["textContent"])
    yuh.write("\n")
    try:
        for d in data["labels"]:
            yuh.write(d["name"]+", ")
    except KeyError:
        continue
    yuh.close()

f.close()