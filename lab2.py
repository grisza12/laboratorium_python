

def zadanie1():
    # "zadanie pierwsze"
    return 0


#konwersja liczby na napis
a=4
b='6'
c= a + int(b)

print c

print 4*7L

print 2.5
print 2e+4
print  4.0/3.0
print 4.0//3.0
print 3.5e+4+1000000L*2

print -2+3j
print 3j**2
print 3j*2
print 3.2+400L/(2+2j)

a,b,c,d,e = 1,3,7,4,6
a+=2
b-=2
c*=2
d/=2

print a,b,c,d,e

# imie = raw_input("Jak masz na imie?\n")
#
# print imie

# a=6
# b=5
# if  a<4:
#     print a
# elif a>4:
#     print b
#
# for x in range(-10,11):
#     print "%+i" % x,
#
# print "\n"
#
# for x in range(5,100,10):
#     print "%3i%6o%5x" % (x,x,x) # wyrownanie do prawej
# for x in range(5,100,10):
#     print "%-3i#-6o%#-5x" % (x,x,x) #wyrownanie do lewej #- wlasciwy prefix
# for x in range(5,100,10):
#     print "%3i %04o %#04x" % (x,x,x) #0 - pole przeznaczone na liczby bedzie wypelnione zerami

# a=[1,2,3,4,5,6]
# while a:
#     a=a[:len(a)-1]
#     print a


def pierw(n):
    return n**0.5
print pierw(3)

def pierw2(n):
    if  n>=0: return n**0.5
print pierw2(4)

def pierw3(n):
    if  n>=0 : return n**0.5
    else: return (-n)**0.5*1j

print pierw3(-6)

def rs(a,b):
    return a-b,a+b
print rs(8,4)

def suma(*arg):
    s=0
    for x in arg:
        s+=x
    return s

print suma(*range(4))