f1 = open("./poidata/train负4.txt", "r", encoding='utf-8')
f2 = open("./poidata/train负5.txt", "w", encoding='utf-8')
for i, j in enumerate(f1):
    # print(j)
    if i % 5 == 0:
        f2.write(j)