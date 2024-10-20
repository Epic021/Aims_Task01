import pandas as pd
import numpy as np
import Ordy
import One_Hot_ordy 

# Code was showing a warning for Downcasting in pandas to remove it in future versions 
pd.set_option('future.no_silent_downcasting', True)


# DataFrame
new_df = {
    "name": ['yash', 'sameer', 'mayank', 'kartik', 'aarya', 'nidhi', 'vikram', 'riya', 'tanya', 'rohit'],
    "age": [28, 30, 27, 25, 30, 27, 24, 29, 26, 29],
    "location": ['delhi', 'pune', 'agra', 'bombay', 'jaipur', 'goa', 'mumbai', 'chennai', 'kolkata', 'hyderabad'],
    "score1": ['low', 'medium', 'low', 'high', 'medium', 'low', 'high', 'low', 'medium', 'high'],
    "score2" : ['bad', 'bad', 'ok', 'ok', 'good', 'good', 'bad', 'ok', 'good', 'bad']

}

Database = pd.DataFrame(new_df)
print("YOUR DATABASE : \n ")
print(Database)

task = int(input("Enter 1 for Ordinal Encoding and 2 for One Hot Encoding : "))


if task == 1 : 
    Ordy.Ordy_encoding(Database)

elif task == 2 :
    One_Hot_ordy.OH_encoding(Database)

else :
    print("Wrong Input")
    