# Program Name:		Wind Chill
# Program Author:	Scott Forsberg
# Creation Date:	2019-01-23
# Class:		CSE 110
# Python Version:	3.7.1

# wind chill formula:
# 35.74 + 0.6215 x T - 35.75 x V**0.16 + 0.4275 x T x V**0.16
# Rows represent wind speed for 0 to 50 in 5 mph increments.
# Columns represent temperatures from -20 to +60 in 10-degree increments



class WindChill:
    
    def __init__(self,temperature,wind):
        
        self.temperature=temperature
        self.wind=wind
        self.chill = int(35.74 + 0.6215 * temperature - 35.75 * wind**0.16 + 0.4275 * temperature * wind**0.16)
