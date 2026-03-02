import random
sk=[-24, -10, 2, 6]
skaitli=[]
for i in range(7):
    sk1=random.randint(-13,20)
    skaitli.insert(i,sk1)
print(skaitli)
#sarakstu apvienošana
skaitli+=sk #skaitli=skaitli+sk
#skaitli.extend(sk)


skaitli.append(-23)
skaitli.insert(2,-19)
print(skaitli)
skaitli.remove(skaitli[5])
print(skaitli)

datne=open("skaitli.txt","w",encoding="utf-8")
datne.write(str(skaitli))
datne.close()
print(f"min={min(skaitli)}")
print(f"max={max(skaitli)}")
print(f"vid={min(skaitli)}")
print(f"vid={sum(skaitli)/len(skaitli)}")