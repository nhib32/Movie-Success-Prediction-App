import pandas as pd 
import os 

csv_file = "Data/User.csv"

def Profile(user):
    print("\n==== User Profile ====")
    print(f"Username:     {user['username']}")
    print(f"Name:         {user['first_name']} {user['last_name']}")
    print(f"DOB:          {user['DOB']}")
    print(f"Email:        {user['email']}")
    print(f"Phone:        {user['phone_number']}")
    print("======================\n")
