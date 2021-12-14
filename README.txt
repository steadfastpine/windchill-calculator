
                         
         .---.           
        /. ./|           
     .-'-. ' |   ,---.   
    /___/ \: |  /     \  
 .-'.. '   ' . /    / '  
/___/ \:     '.    ' /   
.   \  ' .\   '   ; :__  
 \   \   ' \ |'   | '.'| 
  \   \  |--" |   :    : 
   \   \ |     \   \  /  
    '---"       `----'   



Windchill Calculator



# Contact: https://www.linkedin.com/in/steadfastpine/

# Release Date: 2019-06-08
# Version: .2



Description

	Output a table of wind chill values



Prerequisites

	Python 3



Installation

	Download and unzip the program files, then change working directory to them:
	
		# cd windchill-calculator



		# Import the windchill.py file from your python script

		from windchill import *


		# Create an object from the class, input the temperature and wind speed
		# Format: WindChill(teperature,wind)

		test1 = WindChill(50,10);


		# Print the final calculated windchill rating
		print(test1.chill)


		# Print input temperature
		print(test1.teperature)


		# Print input wind speed
		print(test1.wind)



License 

	This program is licensed under the GPL License, view the LICENSE.md file for more information.














