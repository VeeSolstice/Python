""" 
Amount = P( 1 + R/100)**T
Compound Interest (CI)= Amount - P
"""

principal = float(input("Enter the principla amount: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the time: "))

amount1 = principal * (1 + rate/100) ** time
amount2 = principal * pow((1 + rate/100),time)

ci1 = amount1 - principal
ci2 = amount2 - principal

print("Compound Interest according to 1st method:", round(ci1))
print("Compound Interest according to 2nd method:", round(ci2))