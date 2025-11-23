import csv
from AddMovie import main as add_movie
from DisplayMovieList import display_movies
from SearchMovie import search_movie 
from Profile import Profile

def validate_user(username, password):
    try:
        with open("Data/Users.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == username and row["password"] == password:
                    # Convert role to int, keep everything else as string
                    row["role"] = int(row["role"])
                    return row    # return the whole user dictionary
        return None
    except FileNotFoundError:
        print("Error: users.csv not found!")
        return None


def display_menu_as_staff(current_user):
    print("\nStaff Menu:")
    print("1. Profile")
    print("2. View Movie List")
    print("3. Add Movie")
    print("4. Logout")
    staff_choice = input("Enter your choice (1-3): ")
    if staff_choice == '1':
        Profile(current_user)
        display_menu_as_staff(current_user) 
    elif staff_choice == '2':
        display_movies()
        display_menu_as_staff(current_user)
    elif staff_choice == '3':
        add_movie()
        display_menu_as_staff(current_user)
    else:
        print("Logging out...")
        return
    
def display_menu_as_user(current_user):
    print("\nUser Menu:")
    print("1. Profile")
    print("2. Search Movies")
    print("3. View Movies List")
    print("4. Logout")
    user_choice = input("Enter your choice (1-3): ")
    if user_choice == '1':
        Profile(current_user)
        display_menu_as_user(current_user)
    elif user_choice == '2':
        search_movie() 
        display_menu_as_user(current_user)
    elif user_choice == '3':
        display_movies()
        display_menu_as_user(current_user)
    else:
        print("Logging out...")
        return
    
def display_menu_as_guest():
    print("\nGuest Menu:")
    print("1. View Movies List")
    print("2. Exit")
    guest_choice = input("Enter your choice (1-2): ")
    if guest_choice == '1':
        display_movies()
    else:
        print("Exiting the application. Goodbye!")
        exit()