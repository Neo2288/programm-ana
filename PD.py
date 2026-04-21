import json
import csv
with open("uzd1.json",encoding="utf-8") as datne:
    dati=json.load(datne)
#print(type(dati))
valstis=[]
lauksaimniecibas_ipatsvars=[]
for i in dati:
    valstis.append(i["nosaukums"])
    lauksaimniecibas_ipatsvars.append((i["lauksaimniecibas_zeme"]/(i["lauksaimniecibas_zeme"]+i["mezs"]+i["cita_veida_zeme"]))*100)
print(valstis)
print(lauksaimniecibas_ipatsvars)

