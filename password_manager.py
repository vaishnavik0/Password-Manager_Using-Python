# point of this program is to organize and store your password so we gonna store all the passwords along with username of the account they are associated with any text file but we are not going to store the password in plane text but we are going to encrypt the password .
# Now, even though we are encrypting these passwords which means they are going to need a kind of password to be able to decrypt them.
# So its like a master password for all the passwords.
# Also this is not a secure way of storing your passwords do no rely on this other then just a python project.

# First thing: We gonna write the code thats allowing us to actually ask the user whether they want to list out there passwords or whether they want to add a new one
# so we gonna store all of these in a text file 

# ask the user for master passwords

from cryptography.fernet import Fernet

master_pawd = input("What is the master password ? ")


# funcation is executiable and resuable block of code 
# we can call the funcation n number of times whatever is inside the function will always print
def view():
    # pass # Pass keyword does nothing just to avoid indentation error
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user , passw = data.split("|")
            print("User:" , user, ",  Password:" , passw)
            # split() method in Python split a string into a list of strings after breaking the given string by the specified separator.
            # The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.




def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt','a') as f:
        f.write(name + "|" + pwd + "\n")

    

# what i want oto do is create a new file if the file storing our password does not exist and add the password into in
# 1st we will get the username , password and add into it
 

while True:
    mode = input("Would you like to add a new password or view existing ones (view,add), press q to quit? ").lower()

    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode.")
        continue