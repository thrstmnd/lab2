mesto=input("vvedite nomer mesta")
if int(mesto)>54 or int(mesto)<1:
    print("nepravilniy nomer mesta")
elif int(mesto)>36 and int(mesto)<55:
    if int(mesto)%2==1:
        print("bokovoe snizu")
    else:
        print("bokovoe sverhu")
elif int(mesto)>=1 and int(mesto)<37:
    if int(mesto)%2==1:
        print("v kupe snizu")
    else:
        print("v kupe sverhu")