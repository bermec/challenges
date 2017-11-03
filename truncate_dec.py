# If you use deimcal, you need to import
from decimal import getcontext, Decimal

# Set the precision.
getcontext().prec = 3

# Execute 1/7, however cast both numbers as decimals
output = 116/Decimal(3)

# Your output will return w/ 6 decimal places, which
# we set above.
print(output)
print(54/Decimal(5.9))
print(Decimal(54.8/5.9))