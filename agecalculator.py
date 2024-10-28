# Function to calculate the year the user turns 100
def calculate_hundred_year(year, age):
    return year + (100 - age)

# Main program
def main():
    # Get the current year
    from datetime import datetime
    current_year = datetime.now().year
    
    # Ask for user input
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    
    # Calculate the year when the user will turn 100
    year_hundred = calculate_hundred_year(current_year, age)
    
    # Display the result
    print(f"{name}, you will turn 100 years old in the year {year_hundred}.")

# Run the program
if __name__ == "__main__":
    main()
