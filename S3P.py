# Write a Python program that defines a function f(x) that returns x**3 + 8. In the main function of the program, call f(x) with x = 9 and print the result.  Use an if statement that executes if the result is larger than 27 and prints “YAY!”.
#def the fuction 
def f(x):
    return x**3 + 8

def main():
    x = 9
    result = f(x)
    print(f"f({x}) = {result}")
# to see if its chaks out 
    if result > 27:
        print("YAY!")
# print yay 
if __name__ == "__main__":
    main()
# the internet is an amzing place i thought this was gonna be alot harder 
