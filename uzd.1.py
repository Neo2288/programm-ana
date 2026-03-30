import csv
datne=open("kontakti.csv",encoding="utf-8")
kontakti=list(csv.reader(datne))
datne.close()

galvene=["vārds", "uzvārds", "telefons", "pilsēta"]
for i in kontakti:
    print(i[0],i[-2])
with open("k1.csv","w",newline="", encoding="utf-8") as fails:
    a=csv.writer(fails)
    a.csv.writerow(galvene)
