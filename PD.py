#
for i in range(4,10):
    v=input("ievadi vārdu:")
    if len(v)<4:
        continue
    else:
        print(f"Virknē {v.capitalize()} ir {len(v)} simbolu")



