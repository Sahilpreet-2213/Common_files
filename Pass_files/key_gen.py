import random,string 

extra=string.printable[62:93]
num=string.printable[:9]
char=string.printable[10:35]
Char=string.printable[36:61]

store,Store=list(),list()
for x in num:
    store.append(x)   
for x in extra:
    Store.append(x+random.choice(extra))

a=tuple(store)
b=tuple(Store)



if __name__ == "__main__":
    for x,y in zip(a,b):
        main=((x,y))
        main=str(main)+','
        print(main)