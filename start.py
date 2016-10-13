
import time
#
# print "222"
#
# a, b, c = 9, 8, 7
#
# print a, b, c
#
# del a # usuwanie zmiennych
#
# calkowita = 10
# print calkowita
#
# zmiennoprzecinkowa = 10.123
# print zmiennoprzecinkowa
#
# zespolona = 3+5j
# print zespolona
#
# osemkowa =0o15
# print osemkowa
#
# szesnastkowa = 0xabc
# print szesnastkowa
#
# dwojkowa = 0b1011
# print dwojkowa
#
# napis = 'To jest \' String'
# print napis
#
# napis2="Tekst z tabulatorem \t znakiem \n nowego wiersza"
# print napis2
#
# napis3='''
# wiersz
# o wielu
# wierszach
# '''
# print napis3
#
# print ("Zielone "+"jablko")
#
# print ("B"+"a"*5+"rdzo pyszne!")
#
# print ("Py" "thon")
#
'''
Czas
'''
# print xml.utils.iso8601.tostring(time.time())  # returns "2004-04-10T04:44:08.19Z"
# print xml.utils.iso8601.parse("2004-04-09T21:39:00-08:00")  # -8:00 for Seattle, WA
# print xml.utils.iso8601.ctime(0)  # returns "1969-12-31T16:00-08:00"

napis = "Wiek: " +str(18)

print napis

print napis.replace("W","w")

print napis.upper()

napis="Ta liczba %f to %s" %(3.23,"liczba")
print napis

print '{0}, {1}, {2}'.format('a', 'b', 'c')

napis = "123 sdgf DD xx pp le"
print napis.replace(" ","")


'''
LISTY I KROTKI
ilosc elementow jest stala w krotkach
'''

l=[1,2,'element',3.14]
print l

k=(1,2,'element',3.14)
print k

print l[1:3]
print k[:-2]

print l in l

l[0]=3
print l

l[1:3]=['a','b']
print l

macierz = [1,[1,2,3,4]]
print macierz
print macierz[1][3]
macierz[1][3]=5
print macierz

"""
Listy modyfikowanie
"""

lista=[1,2,3]
lista2=lista+[4,5,6]
print lista2

lista=[4,6,2,4,8]
print lista
lista.sort()
print lista
lista.reverse()
print lista
lista.append(6)
print lista
print lista
lista.pop()
print lista
lista.remove(4)
print lista

del lista[1:3]
print lista

"""
Slowniki
"""

slownik = {'a':'b','klucz':15,3:[1,3,4]}
print slownik

print list(slownik.keys())

d={}
print 'b' in d

d['b']=1
print d

"""
Boolean
"""

a=True
b=False
print a,b

x=4
y=8

print x<y
print x==y
print x!=y

print a or b
print a and b
print not a
print not b


"""
Petle
"""

licznik = 10
wartosc = 15

while licznik <= wartosc:
    licznik += 1
    print "Jestem w petli"

for i in range(10):
    print i

bar = {"imie":"tomasz","nazwisko":"lobuz"}
print bar["imie"]

for i in bar:
    print i + " - " + bar[i]
if  bar.has_key("imie"):
    print bar["imie"]
print bar.get("imie", "Brak klicza")

