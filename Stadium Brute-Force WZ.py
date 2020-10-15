def check_room(code):
    
    assert len(code)==8

    room=""
    c=0
    n=0
    h=0
    for i in code:
        if i=="c":
            c=c+1

        elif i=="n":
            n=n+1

        elif i=="h":
            h=h+1

    if c==0 and n==3 and h==2:
        room="china"

    elif c==1 and n==2 and h==2:
        room="nose"

    elif c==1 and n==3 and h==1:
        room="house"

    assert room=="china" or room=="nose" or room=="house"

    return room


def skip_check(c1,c2):

    room1,room2,skip,c,n,h="","",False,0,0,0
    
    for i in c1:
        if i=="c":
            c=c+1

        elif i=="n":
            n=n+1

        elif i=="h":
            h=h+1

    if c==0 and n==3 and h==2:
        room1="china"

    elif c==1 and n==2 and h==2:
        room1="nose"

    elif c==1 and n==3 and h==1:
        room1="house"

    c,n,h=0,0,0


    for i in c2:
        if i=="c":
            c=c+1

        elif i=="n":
            n=n+1

        elif i=="h":
            h=h+1

    if c==0 and n==3 and h==2:
        room2="china"

    elif c==1 and n==2 and h==2:
        room2="nose"

    elif c==1 and n==3 and h==1:
        room2="house"

    if room1!="" and room2!="" and room1!=room2:
        skip=True

    return skip




def china_room(code):

    print()
    print("LUCKY CODE! EASY TO BRUTE-FORCE")
    
    num=["0","1","2","3","4","5","6","7","8","9"]
    lis_h=""
    x=0
    
    for i in num:
        found=False
        for f in code:
            if f==i:
                found=True
        if not found:
            lis_h=lis_h+str(i)

    for h in lis_h:
        lis_n=""
        for i in lis_h:
            if i!=h:
                lis_n=lis_n+i
                
        for n in lis_n:
            cpt=0
            comb=""
            for i in code:
                
                if i.isdigit():
                    comb=comb+i
                elif i.isalpha:
                    if i=="h":
                        comb=comb+h
                    elif i=="n":
                        comb=comb+n
                        
                cpt=cpt+1
                if cpt==4:
                    comb=comb+" "
            print()
            print("  ",comb)
            x=x+1

        lol=input("")
        print()
        print()
        print()
    print(x, "combinations")
                    
                
              
def nose_room(code):

 
    x=0
    num=["0","1","2","3","4","5","6","7","8","9"]
    lis_n=""
    lis_c=""

    for i in code:
        if i.isdigit():
            lis_n=lis_n+i

    for i in num:
            found=False
            for f in code:
                if f==i:
                    found=True
            if not found:
                lis_c=lis_c+str(i)

    for n in lis_n:

        for c in lis_c:
            lis_h=""
            
            for i in lis_c:
                if i!=c:
                    lis_h=lis_h+i
          
            for h in lis_h:
                cpt=0
                comb=""
                for i in code:
                    
                    if i.isdigit():
                        comb=comb+i
                    elif i.isalpha:
                        if i=="c":
                            comb=comb+c
                        elif i=="n":
                            comb=comb+n
                        elif i=="h":
                            comb=comb+h
                            
                    cpt=cpt+1
                    if cpt==4:
                        comb=comb+" "
                print()
                print("  ",comb)
                x=x+1

            input()
        print()
        print()
        print()
        
    print(x, "combinations")



def house_room(code):

    x=0
    num=["0","1","2","3","4","5","6","7","8","9"]
    lis_h=""
    lis_c=""

    for i in code:
        if i.isdigit():
            lis_h=lis_h+i

    for i in num:
            found=False
            for f in code:
                if f==i:
                    found=True
            if not found:
                lis_c=lis_c+str(i)

            
    for h in lis_h:

        for c in lis_c:
            lis_n=""
            
            for i in lis_c:
                if i!=c:
                    lis_n=lis_n+i
          
            for n in lis_n:
                cpt=0
                comb=""
                for i in code:
                    
                    if i.isdigit():
                        comb=comb+i
                    elif i.isalpha:
                        if i=="c":
                            comb=comb+c
                        elif i=="n":
                            comb=comb+n
                        elif i=="h":
                            comb=comb+h
                            
                    cpt=cpt+1
                    if cpt==4:
                        comb=comb+" "
                print()
                print("  ",comb)
                x=x+1

            input()
        print()
        print()
        print()
        
    print(x, "combinations")
        



def code1(c1):
    room=check_room(c1)

    if room=="china":
        china_room(c1)

    elif room=="nose":
        nose_room(c1)

    elif room=="house":
        house_room(c1)
    




def code2(c1,c2):

    room1=check_room(c1)
    room2=check_room(c2)
    assert room1!=room2

    c,n,h=-1,-1,-1

    for i in range(8):
        if c1[i].isalpha() and c2[i].isdigit():
            if c1[i]=="c":
                c=int(c2[i])
            elif c1[i]=="n":
                n=int(c2[i])
            elif c1[i]=="h":
                h=int(c2[i])

        if c2[i].isalpha() and c1[i].isdigit():
            if c2[i]=="c":
                c=int(c1[i])
            elif c2[i]=="n":
                n=int(c1[i])
            elif c2[i]=="h":
                h=int(c1[i])


    if c==-1:
        stk="c"

    if n==-1:
        stk="n"
        
    if h==-1:
        stk="h"

    code=""

    for i in c1:
        if i.isdigit():
            code=code+i
        elif i.isalpha():
            
            if i=="c" and c>-1:
                code=code+str(c)
                
            elif i=="n" and n>-1:
                code=code+str(n)
                
            elif i=="h" and h>-1:
                code=code+str(h)
                
            else:
                code=code+i

    num=["0","1","2","3","4","5","6","7","8","9"]
    lis=""

    for i in num:
        found=False
        for f in code:
            if f==i:
                found=True
        if not found:
            lis=lis+str(i)


    for i in lis:
        bforce_code=""
        cpt=0
        
        for f in code:
            if f==stk:
                bforce_code=bforce_code+i
            else:
                bforce_code=bforce_code+f
                
            cpt=cpt+1
            if cpt==4:
                bforce_code=bforce_code+" "
            
        print()
        print("  ",bforce_code)

        

c1=input("code 1: ")
c2=input("code 2: ")
numb=""

if skip_check(c1,c2):
    numb="2"

if c2=="":
    numb="1"

while numb!="1" and numb !="2":
    numb=input("Indicate if 1 or 2 codes: ")
    if numb!="1" and numb!="2":
        print('Invalid, please choose between "1" and "2".')

if numb=="1":
    code1(c1)
    
elif numb=="2":
    code2(c1,c2)

    
    

