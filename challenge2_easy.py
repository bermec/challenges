''' Hello, coders! An important part of programming is being able to apply your programs,
 so your challenge for today is to create a calculator application that has use in your life.
 It might be an interest calculator, or it might be something that you can use in the
 classroom. For example, if you were in physics class, you might want to make a F = M * A calc.

EXTRA CREDIT: make the calculator have multiple functions! Not only should
it be able to calculate F = M * A, but also A = F/M, and M = F/A!

'''

print( "Ohm's Law")

choice = input('Looking for volts, amps or resistance? input v, i or r ')

if choice == 'v':
    amps = input('Amps? ')
    res = input('Resistance? ')
    volts = float(amps) * float(res)
    print('Thee voltage you are looking for is {0} volts'.format(volts))


elif choice == 'i':
    volts = input('Volts? ')
    res = input('Resistance? ')
    amps = float(volts) / float(res)
    print('Thee amperage you are looking for is {0} amps'.format(amps))

else:
    choice == 'r'
    amps = input('Amps? ')
    volts = input('Volts? ')
    res = float(volts) / float(amps)
    print('Thee resistance you are looking for is {0} ohms'.format(res))




























