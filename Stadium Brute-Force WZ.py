def check_room(code):
    
    room=""
    c=0
    n=0
    h=0
    valid=False
    dgt_lis=[]
    dgt_cpt=0
    
    for i in code:

        if not i.isdigit() and i!="c" and i!="n" and i!="h":
            c,n=0,0
            break
        
        if i.isdigit():
            dgt_lis.append(i)

        
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

    if room=="china" or room=="nose" or room=="house":
        valid=True

    if len(code)!=8:valid=False

    for i in dgt_lis:
        for f in dgt_lis:
            if f==i:
                dgt_cpt+=1
                
    if dgt_cpt>3:valid=False

    return (room,valid)


def skip_check(c1,c2):

    room1,room2,skip="","",False
   
    room1=check_room(c1)
    room2=check_room(c2)

    if room1[0]!=room2[0] and room1[1]==room2[1]==True:
        skip=True

    for i in range(8):

        char1=c1[i]
        char2=c2[i]
        
        if char1.isalpha() and char2.isalpha() and char1!=char2:
            skip=False
            break
        
        elif char1.isdigit() and char2.isdigit() and char1!=char2:
            skip=False
            break

    return skip


def print_list(lis):
    
    lim=len(lis)
    ind_stk=0

    for cpt in range(lim):

        x=cpt
        ind_stk=cpt
        stk=lis[cpt]

        for i in lis[cpt:]:

            if int(i)<int(stk):

                ind_stk=x
                stk=i
                
            x=x+1

        tamp=lis[cpt]
        lis[cpt]=lis[ind_stk]
        lis[ind_stk]=tamp

    cpt=0

    while lim>cpt:
        for i in range(6): 
            
            print()
            print("  " + lis[cpt][:4] + " " + lis[cpt][-4:])
                
            cpt=cpt+1

        input()
        print()
        print()
        print()




def china_room(code):

    print()
    print("LUCKY CODE! EASY TO BRUTE-FORCE")
   
    num=["0","1","2","3","4","5","6","7","8","9"]
    lis_h=""
    lis=[]
   
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
            
            comb=""
            for i in code:
               
                if i.isdigit():
                    comb=comb+i
                elif i.isalpha:
                    if i=="h":
                        comb=comb+h
                    elif i=="n":
                        comb=comb+n

            lis.append(comb)
                
    print_list(lis)

    print("42 combinations")
                   
               
             
def nose_room(code):

    num=["0","1","2","3","4","5","6","7","8","9"]
    lis_n=""
    lis_c=""
    lis=[]

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

        lis=[]

        for c in lis_c:
            lis_h=""
           
            for i in lis_c:
                if i!=c:
                    lis_h=lis_h+i
         
            for h in lis_h:
        
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
                           
                lis.append(comb)

        print_list(lis)

    print("126 combinations")



def house_room(code):

    num=["0","1","2","3","4","5","6","7","8","9"]
    lis_h=""
    lis_c=""
    lis=[]

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

        lis=[]

        for c in lis_c:
            lis_n=""
           
            for i in lis_c:
                if i!=c:
                    lis_n=lis_n+i
         
            for n in lis_n:
            
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
                           
                lis.append(comb)

        print_list(lis)

    print("126 combinations")
       


def code1(c1):
    room=check_room(c1)[0]

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
        print(bforce_code)

valid=False
     
while not valid:
    
    c1=input(("code 1: ")).lower()
    c2=input(("code 2: ")).lower()

    if c2=="":
        if check_room(c1)[1]:
            valid=True
            code1(c1)

    elif skip_check(c1,c2):
        valid=True
        code2(c1,c2)

    if not valid:
        print()
        print("INVALID CODE(S). TRY AGAIN.")
        print()

