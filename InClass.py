# Ex 1: Create a variable and assign a value
name = "Alyssa"

# Ex 2: Create another variable with a number

num = 12

# Ex 3: Print text on the screen
print("Sup world? ")

# Ex: 4: Print what the variable name has inside

print(name)

# Ex 5: Print a sentence using the variable name

print("my name is " + name)


# Ex: 6: Change the value of the variable and print again

name = "Aly" 
print("My nickname is " + name)
print(f"Hello world, I loveeee cheese {name}")

# Ex: 7: Ask user for fav animal

print("What is your favorite animal? ")
animal = input()
print("I didn't know that", animal, "was your favorite animal")

# Ex 8: Use the variable created in Ex 1
# If the variable is greater than 10 print a message
# Otherwise create another message bc yes

if num>10:
    print("Congrats, your number is greater than 10!")
else:
    print("Sorry, your number is not greater than 10")
