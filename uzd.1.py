import json
with open("skoleni_atzimes.json",encoding="utf-8") as datne:
    dati=json.load(datne)
    vardi=[]
    for i in dati:
       #print(i["name"])
       vardi.append(i["name"])
vardi.sort()
print(vardi)
for i in dati:
    # print(i["name"])
    #vardi.append(i["name"])
    #print(i["grades"]["Fizika"])
    if i["grades"]["Fizika"] < 4:
        print(i["name"])
for i in dati:
    vid=(i["grades"]["Matematika"]+i["grades"]["Fizika"]+i["grades"]["Informatika"])/3
    print(i["name"],":",vid)
for i in dati:
    i["grades"].update({"Sports":8})
    print(i["grades"])
mat=[]
a=0
for i in dati:
    mat.append(i["grades"]["Matematika"])
print("min",min(mat))
print("max",max(mat))
print("10:",mat.count(10))

v=input("skolēna vārds:")
for i in dati:
    i.get(v,"Skolēna nav")
    print()