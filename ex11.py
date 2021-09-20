n = int(input("Dati nr de elemente din vector = "))
a=[]
if n < 10 and n>0:
    print('Introduceti  ',n, " elemente pt vectorul creat")
    for i in range(0, n):
        n1=int(input("Dati elementul = "))
        a.extend([n1])
    o = a.copy()
    print("a)afişează pe ecran componentele tabloului la un interval de 5 poziţii")
    print("     ".join(map(str, a)))
    print("b)afişează pe ecran numerele în ordinea inversă a introducerii în calculator")
    print(a[::-1])
    print("c)sortează componentele tabloului în ordine descrescătoare")
    print(a.sort(reverse=True))
    print("d)afişează pe ecran doar componentele pare")
    d=[]
    for z in range(0, len(a)):
        if a[z]%2==0:
            y=a[z]
            d.extend([y])
    print(d)
    print("afişează pe ecran media aritmetică a componentelor pare")
    if len(d)>0:
        print(sum(d)/len(d))
    print("f)afişează pe ecran doar componentele impare")
    listaf=[]
    for i in range(0, len(a)):
        if a[i]%2!=0:
            elemf=a[i]
            listaf.extend([elemf])
    print(listaf)
    print("g)afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură)")
    x=eval(input("Introdu x  = "))
    y=eval(input("Introdu y  = "))
    listag=[]
    for f in range(0, len(a)):
        if a[f]>x and a[f]%y!=0:
            t = a[f]
            listag.extend([t])
    print(listag)
    print("h)afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură)")
    listah=[]
    for h in range(0, len(a)):
        if a[h]>x and a[h]<y:
            elemh = a[h]
            listah.extend([elemh])
    print(listah)
    print("i)afişează pe ecran poziţiile (indicii) componentelor impare negative")
    listai=[]
    for elemi in o:
        if elemi<0 and elemi%2!=0:
            l = o.index(elemi)
            listai.extend([l])
    print(listai)
    print("j)afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative")
    listadouacifre = []
    for elements in o:
        if elements/10>=1 and elements/10<10:
            m = o.index(elements)
            listadouacifre.extend([m])
    print(listadouacifre)
    print("k)înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv")
    minimum = min(o)
    p=[]
    p = o[:]
    p[0] = minimum
    print(p)
    print("l)înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia")
    n=[]
    n = o[:]
    indexmin = o.index(minimum)
    n[indexmin] = n[0]
    print(n)
    print("m)	creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatura")
    print(d)
    print("n)	 creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură")
    newlist=[]
    for divtrei in o:
        if divtrei%3==0:
            newlist.extend([divtrei])
    print(newlist)
   

else:
    print("numarul elementelor trebuie sa fie intre 0 si 10")
