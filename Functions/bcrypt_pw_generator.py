import bcrypt

password = "1Qay2Wsx!"

# Hash the password
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

print("Hashed password:", hashed_password)