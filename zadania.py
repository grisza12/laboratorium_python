import sys


def poleTrojkata():
    #"Obliczanie pola trojkata"

    wysokosc = raw_input("Podaj wysokosc trojkata")
    podstawa = raw_input("Podaj podstawe trojkata")

    return float(wysokosc)*float(podstawa)*0.5

def wyswietlTabliczeMnozenia():

    a=[1,2,3,4,5,6,7,8,9,10]

    for i in a:
        for j in a:
            print (i*j),
        print "\n"

    return ""
def ciagFib(n):

    a=1
    b=1
    c=a+b
    temp=2

    print a,b,
    while temp<n:

        c=a+b
        print c,
        a=b
        b=c
        temp+=1
    return ""

# print (poleTrojkata())
# print wyswietlTabliczeMnozenia()
print ciagFib(5)

