import csv
import pandas as pd 
import os 

csv_file = "Data/Predicted.csv"

def search_movie(role):
    print('.\nEnter movie title:')
    title = input("Title: ")

    # Check if file exists
    if not os.path.exists(csv_file):
        print("CSV file not found!")
        return
    
    # Read CSV using pandas
    df = pd.read_csv(csv_file)

    movie = df[df['title'].str.lower() == title.lower()]

    if not movie.empty:
        print("\nMovie found:")
        print(movie.to_string(index=False))
    else:
        print("\nMovie not found.")

    if role == 2 and not movie.empty:
        print("Do you want to buy the ticket for this movie?")