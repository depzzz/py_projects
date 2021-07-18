import os

os.chdir("5_minute_crafts/ha")

print("Starting......")
for index, filename in enumerate(os.listdir()):
    os.rename(f"{os.getcwd()}/{filename}",f"{os.getcwd()}/{index}.txt")

print("Done.......")