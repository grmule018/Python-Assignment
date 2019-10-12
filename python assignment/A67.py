kpa = float(input("Enter pressure in kilopascal: "))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("The pressure in pounds per square inch:",psi)
print("The pressure in milimeter of mercury:",mmhg)
print("Atmospheric pressure:",atm)
