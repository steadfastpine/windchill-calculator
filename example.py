# This example demonstrates usage of the WindChill class.


# Import the windchill.py file

from windchill import *


# Create an object from the class, input the temperature and wind speed
# Format: WindChill(teperature,wind)

test1 = WindChill(50,10)


# Print the final calculated windchill rating
print(test1.chill)


# Print input temperature
print(test1.temperature)


# Print input wind speed
print(test1.wind)
