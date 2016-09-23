print " ...Welcome to FizzBuzz..."

vnesena_stevilka = int(raw_input("Vnesite stevilo med 1 in 100: "))

print "Vnesena stevilka je: "+str(vnesena_stevilka)

a = 0

for a in range(vnesena_stevilka):

    a = a + 1

    if a % 3 == 0 and a % 5 == 0:
        print "fizzbuzz"

    elif a % 3 == 0:
        print "fizz"

    elif a % 5 == 0:
        print "buzz"

    else:
        print a

print "Program closed..."
