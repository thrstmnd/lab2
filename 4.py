zvet1=input("vvedite perviy zvet")
if zvet1 != "krasniy" and zvet1 != "zeltiy" and zvet1 != "siniy":
    print("ne verniy zvet")
else:
    zvet2=input("vvedite vtoroy zvet")
    if zvet2 != "krasniy" and zvet2 != "zeltiy" and zvet2 != "siniy":
        print("ne verniy zvet")
    else:
        if zvet1 == "krasniy" and zvet2 == "krasniy":
            print("krasniy")
        elif zvet1=="siniy" and zvet2=="siniy":
            print("siniy")
        elif zvet1=="zeltiy" and zvet2=="zeltiy":
            print("zeltiy")
        elif (zvet1=="krasniy" and zvet2=="siniy") or (zvet1=="siniy" and zvet2=="krasniy"):
            print("fioletoviy")
        elif (zvet1=="krasniy" and zvet2=="zeltiy") or (zvet1=="zeltiy" and zvet2=="krasniy"):
            print("oranjeviy")
        elif (zvet1=="siniy" and zvet2=="zeltiy") or (zvet1=="zeltiy" and zvet2=="siniy"):
            print("zeleniy")