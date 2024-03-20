god=input("vvedite god")
if int(god)%4==0 and int(god)%100!=0 or int(god)%400==0:
    print("god",god,"visokosniy")
else:
    print("god",god,"nevisokosniy")