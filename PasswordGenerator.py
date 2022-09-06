from codecs import charmap_decode
import random
import string

# Characters to generate password from

chars=list(string.ascii_letters+string.digits+"!@#$%^&*()")

def generate_random_password():
    #length of password from user
    length= int(input("Enter Password Length:"))
    if length > 0 :
        random.shuffle(chars)
        password = []
        for i in range(length):
            password.append(random.choice(chars))
            random.shuffle(password)
        print("".join(password))
    else : 
        print("Please enter a number bigger than 0")
        generate_random_password()

      

## invoking the function
generate_random_password()
