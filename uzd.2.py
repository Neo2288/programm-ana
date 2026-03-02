fails=open("vardi.txt","r",encoding="utf-8")
dati=fails.read().split(", ")
print(type(dati))
dati.sort()
print(dati)
for i in dati:
    if i.startswith("r")==True:
        print(i)
    