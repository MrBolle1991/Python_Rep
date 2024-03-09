PASSWORD = "Password1337"
max_attempts = 3
attempt = 0
authenticated = False

num1 = 0


#####

while attempt < max_attempts:
    password = input("Please enter your password: ")

    if password == PASSWORD:
        print("Password correct!")
        num1 = input("Please enter a number between 1-10! ")
        authenticated = True
        break
    else:
        attempt += 1
        remaining_attempts = max_attempts - attempt
        if remaining_attempts > 0:
            print("Wrong password! you have" + ' ' + str(remaining_attempts) + ' ' + 'attempt(s) left')
        else:
            print("You have used the maximum number of attempts. Exiting...")
            quit("Maximum attempts reached!")

if not authenticated:
    quit("Authentication failed. Exiting...")

#####

print(num1)
if int(num1) > 5:
    print("Du stinkst!")
if int(num1) < 5:
    print("Du bist der Beste!") 

