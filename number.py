try:
    a=open("trrry.py","r")
    b=a.read()
    d=open("trrry.py","w")
    c=d.write(str(int(b)+1))
    print(b)

except:
    a=open("trrry.py","w")
    b=a.write("1")
    print("1")