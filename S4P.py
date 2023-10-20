#Write a Python program that declares a class describing your favorite animal. Do the data members of the class represent the following physical parameters of the animal: length of the arms (float), length of the legs (float), number of eyes (int), does it have a tail? (bool), is it furry? (bool). Write an initialization function that sets the values of the data members when an instance of the class is created. Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal.
# Define a Python class to describe my favorite animal.
class FavoriteAnimal:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        # Initialize data members to represent physical parameters.
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    # Create a member function to print and describe the physical characteristics.
    def describe(self):
        print("Physical Characteristics of My Favorite Animal:")
        print(f"Arm Length: {self.arm_length} inches")
        print(f"Leg Length: {self.leg_length} inches")
        print(f"Number of Eyes: {self.num_eyes}")
        print(f"Has Tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is Furry: {'Yes' if self.is_furry else 'No'}")

# Define the main function to create an instance of the class and call the describe function.
def main():
    # Create an instance of the class for my favorite animal (a dog).
    my_favorite_dog = FavoriteAnimal(7, 8.0, 2, True, True)
    
    # Call the describe function to display the characteristics.
    my_favorite_dog.describe()

if __name__ == "__main__":
    # Call the main function when the script is executed.
    main()
