# Write a Python program that writes out a table of the function sin(x) vs. x, where x is tabulated between 0 and 2 with a thousand entries. Follow the basic Python program structure, including a main program function.
# Import the math module for the sine function
import math

# Define a function to generate a table of sine values
def generate_sin_table(start, end, num_points):
    table = []  # Initialize an empty list to store (x, sin(x)) pairs
    step = (end - start) / (num_points - 1)  # Calculate the step size
    x = start  # Initialize the x value with the start value
    for _ in range(num_points):  # Loop through the desired number of points
        sin_x = math.sin(x)  # Calculate the sine of the current x
        table.append((x, sin_x))  # Add (x, sin(x)) to the table
        x += step  # Increment x by the step size
    return table  # Return the generated table

# Define a function to print the sine table
def print_sin_table(table):
    print("x\t\t sin(x)")  # Print a header for the table
    print("----------------------")
    for x, sin_x in table:  # Loop through the table and print values
        print(f"{x:.4f}\t\t{sin_x:.4f}")  # Format and print each (x, sin(x)) pair

# Define the main function
def main():
    start = 0  # Define the start value for x
    end = 2  # Define the end value for x
    num_points = 1000  # Define the number of points to generate
    sin_table = generate_sin_table(start, end, num_points)  # Generate the sine table
    print_sin_table(sin_table) 
     # Print the sine table
if __name__ == "__main__":



