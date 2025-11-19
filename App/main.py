from LogIn import Login

# Movie Success Prediction App Workflow
# Step 1: Display login options: log in, continue as guest or exit =
def main():
    Login()

#   If Search Movies:
#       - Ask for search criteria (title, genre, actor, etc.)
#       - Display matching movies from CSV file

#   After viewing a movie:
#       - Ask whether to book ticket or return to User Menu

#   If Logout:
#       - Return to Login Screen

# If Guest:
#   Display Guest Menu:
#       1. View Predicted Movies
#       2. Exit

#   - Guests can only view movies, no search or booking


if __name__ == "__main__":
    main()
