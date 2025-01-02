import os
import getpass



raw_passwords = ["0", "63720343963993770522", "07490361682184788916", "90462667648717258041", "52257466584862065975", "17852810103515368176", "66741700086909559323", "95841648150912581088", "51731926608264477573", "93434577719959334375", "11234970603274236181", "29989800325720968090", "55318742090183072750", "76956720576496375346", "46399497056262601117", "96707336316577404327", "38944150879302686899", "37309356062372847711", "00938819724143233071", "93565492572306999559", "66577252147617789282"]

my_hash = lambda password: (sum(ord(c) * pow(10, i) for i, c in enumerate(getpass.getuser())) + int(password)) % 1000000
passwords = [my_hash(x) for x in raw_passwords]
print(passwords)
passwords = [(lambda password: (sum(ord(c) * pow(10, i) for i, c in enumerate(getpass.getuser())) + int(password)) % 1000000)(x) for x in raw_passwords]
print(passwords)

def prepare_flag(flagnum: int):

    print(f"Preparing Flag {flagnum}")

    match flagnum:
        case 1:
            try:
                if not os.path.exists("flag01"):
                    os.mkdir("flag01")
                    print(f"Folder 'flag01' created successfully")
                if not os.path.exists("flag01/flag01.txt"):
                    with open("flag01/flag01.txt", "w") as f01:
                        f01.write(str(passwords[flagnum]) + "\n")
                    print(f"File 'flag01.txt' written successfully")


            except Exception as error:
                print("An exception occurred: ", error)


if __name__ == "__main__":

    exit()

    print(f"Hello, {getpass.getuser()}! Welcome to the CSCI1133 Capture The Flag!")

    current_directory = os.getcwd()
    if current_directory.split('/')[-1] != "CSCI1133-CTF":
        print("Please make sure you are in the CSCI1133-CTF directory")

    else:

        prepare_flag(1)

        try:
            inpt = int(input('Enter the code you found: '))
            index = passwords.index(inpt)

            print(f"Congratulations! You found flag #{index}")
            if index == len(passwords) - 1:
                print("You have completed the CTF. Please enter your final code into *** for a grade.")
            else:
                prepare_flag(index + 1)
        
        except:
            print("I'm sorry, that flag is not correct")