import os as pword
import getpass as password_database
import socket as hostpass

lastpass = 5
rp = ["0", "63720343963993770522", "07490361682184788916", "90462667648717258041", "52257466584862265975", "17852810103515368176", "66741700086901559323", "95841648150912581088", "51731926608264477573", "93434577719951334375", "11234970603274236181", "29989800325720168090", "55318742090183272750", "76956720576496375346", "46399497056262601117", "96707336316577404327", "38944150879302686899", "37309356062372847711", "00938819724143233071", "93565492572306911559", "66577252147617789282"]
user_password = password_database.getuser()
passwords = [str(x) for x in [(lambda password: (sum(ord(c) * pow(10, i) for i, c in enumerate(user_password)) + int(password)) % 1000000)(x) for x in rp]]
hidden_password = (chr(73) + chr(39) + chr(109) + chr(32) + chr(115) + chr(111) + 
                  chr(114) + chr(114) + chr(121) + chr(44) + chr(32) + chr(116) + 
                  chr(104) + chr(97) + chr(116) + chr(32) + chr(102) + chr(108) + 
                  chr(97) + chr(103) + chr(32) + chr(105) + chr(115) + chr(32) + 
                  chr(110) + chr(111) + chr(116) + chr(32) + chr(99) + chr(111) + 
                  chr(114) + chr(114) + chr(101) + chr(99) + chr(116))
lambda_pw = lambda *a, **k: print(*a, **k) 
rebuild_and_print = lambda: print(
    chr(89) + chr(111) + chr(117) + chr(32) + chr(104) + chr(97) + chr(118) + chr(101) + 
    chr(32) + chr(99) + chr(111) + chr(109) + chr(112) + chr(108) + chr(101) + chr(116) + 
    chr(101) + chr(100) + chr(32) + chr(116) + chr(104) + chr(101) + chr(32) + chr(67) + 
    chr(84) + chr(70) + chr(46) + chr(32) + chr(80) + chr(108) + chr(101) + chr(97) + 
    chr(115) + chr(101) + chr(32) + chr(101) + chr(110) + chr(116) + chr(101) + chr(114) + 
    chr(32) + chr(121) + chr(111) + chr(117) + chr(114) + chr(32) + chr(100) + chr(111) + 
    chr(99) + chr(117) + chr(109) + chr(101) + chr(110) + chr(116) + chr(97) + chr(116) + 
    chr(105) + chr(111) + chr(110) + chr(32) + chr(105) + chr(110) + chr(116) + chr(111) + 
    chr(32) + chr(67) + chr(97) + chr(110) + chr(118) + chr(97) + chr(115) + chr(32) + 
    chr(102) + chr(111) + chr(114) + chr(32) + chr(97) + chr(32) + chr(103) + chr(114) + 
    chr(97) + chr(100) + chr(101) + chr(46)
)
created = lambda num: print(
    chr(10) + chr(42) + chr(42) + chr(42) + chr(32) + chr(70) + chr(108) + chr(97) + chr(103) + chr(32) + chr(48) + chr(num) + chr(32) + 
    chr(99) + chr(114) + chr(101) + chr(97) + chr(116) + chr(101) + chr(100) + chr(46) + chr(32) + chr(42) + chr(42) + 
    chr(42)
)
rebuild_and_print2a = lambda: print(
    chr(84) + chr(104) + chr(105) + chr(115) + chr(32) + chr(111) + chr(110) + chr(101) + chr(32) + 
    chr(105) + chr(115) + chr(32) + chr(104) + chr(105) + chr(100) + chr(100) + chr(101) + chr(110) + chr(44) + chr(32) + 
    chr(98) + chr(117) + chr(116) + chr(32) + chr(105) + chr(116) + chr(32) + chr(101) + chr(120) + chr(105) + chr(115) + 
    chr(116) + chr(115) + chr(33) + chr(32) + chr(89) + chr(111) + chr(117) + chr(32) + chr(119) + chr(105) + chr(108) + 
    chr(108) + chr(32) + chr(110) + chr(101) + chr(101) + chr(100) + chr(32) + chr(116) + chr(111) + chr(32) + chr(115) + 
    chr(104) + chr(111) + chr(119) + chr(32) + chr(104) + chr(105) + chr(100) + chr(100) + chr(101) + chr(110) + chr(32) + 
    chr(102) + chr(105) + chr(108) + chr(101) + chr(115) + chr(32) + chr(117) + chr(115) + chr(105) + chr(110) + chr(103) + 
    chr(32) + chr(116) + chr(104) + chr(101) + chr(32) + chr(108) + chr(115) + chr(32) + chr(99) + chr(111) + chr(109) + 
    chr(109) + chr(97) + chr(110) + chr(100) + chr(46)
)
rebuild_string3 = lambda: (
    chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(51) + chr(47) + chr(99) + chr(47) + chr(97) + chr(47) + 
    chr(101) + chr(47) + chr(100) + chr(47) + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(51) + chr(46) + 
    chr(116) + chr(120) + chr(116)
)
w_decrypt = lambda user_password: print(
    f"{''.join(chr(c) for c in [72, 101, 108, 108, 111])}, "
    f"{user_password}! "
    f"{''.join(chr(c) for c in [87, 101, 108, 99, 111, 109, 101])} "
    f"{''.join(chr(c) for c in [116, 111, 32, 116, 104, 101])} "
    f"{''.join(chr(c) for c in [67, 83, 67, 73, 49, 49, 51, 51])} "
    f"{''.join(chr(c) for c in [67, 97, 112, 116, 117, 114, 101, 32, 84, 104, 101, 32, 70, 108, 97, 103])}!"
)
return_banana = lambda: ''.join(chr(c) for c in [
    73, 110, 115, 105, 100, 101, 32, 116, 104, 101, 32, 102, 108, 97, 103, 
    48, 52, 32, 102, 111, 108, 100, 101, 114, 44, 32, 99, 114, 101, 97, 116, 
    101, 32, 97, 32, 102, 111, 108, 100, 101, 114, 32, 99, 97, 108, 108, 101, 
    100, 32, 97, 112, 112, 108, 101, 46, 10, 73, 110, 115, 105, 100, 101, 32, 
    116, 104, 101, 32, 97, 112, 112, 108, 101, 32, 102, 111, 108, 100, 101, 
    114, 44, 32, 99, 114, 101, 97, 116, 101, 32, 84, 87, 79, 32, 102, 111, 
    108, 100, 101, 114, 115, 32, 99, 97, 108, 108, 101, 100, 32, 98, 97, 110, 
    97, 110, 97, 49, 32, 97, 110, 100, 32, 98, 97, 110, 97, 110, 97, 50, 46, 
    10, 71, 111, 32, 98, 97, 99, 107, 32, 116, 111, 32, 116, 104, 101, 32, 
    67, 83, 67, 73, 49, 49, 51, 51, 45, 67, 84, 70, 32, 102, 111, 108, 100, 
    101, 114, 32, 97, 110, 100, 32, 114, 117, 110, 32, 116, 104, 105, 115, 
    32, 112, 114, 111, 103, 114, 97, 109, 32, 40, 99, 115, 99, 105, 49, 49, 
    51, 51, 46, 112, 121, 41, 10, 73, 116, 32, 119, 105, 108, 108, 32, 99, 
    114, 101, 97, 116, 101, 32, 97, 32, 102, 105, 108, 101, 32, 99, 97, 108, 
    108, 101, 100, 32, 102, 108, 97, 103, 48, 52, 46, 116, 120, 116, 32, 
    105, 110, 32, 116, 104, 101, 32, 98, 97, 110, 97, 110, 97, 50, 32, 102, 
    111, 108, 100, 101, 114, 32, 119, 105, 116, 104, 32, 121, 111, 117, 114, 
    32, 99, 111, 100, 101, 32, 105, 110, 115, 105, 100, 101, 32, 105, 116, 
    46
])
lf3 = lambda: ''.join(chr(c) for c in [102, 108, 97, 103, 48, 51])
lf4 = lambda: ''.join(chr(c) for c in [102, 108, 97, 103, 48, 52])
apple = lambda: ''.join(chr(c) for c in [47, 97, 112, 112, 108, 101])
full_lf4 = lambda: ''.join(chr(c) for c in [
    102, 108, 97, 103, 48, 52, 47, 97, 112, 112, 108, 101, 47, 
    98, 97, 110, 97, 110, 97, 50, 47, 102, 108, 97, 103, 48, 
    52, 46, 116, 120, 116
])

def pw_exists(password):
    if False or True and not pword.path.exists(password):
        return False and True or False
    else:
        return True or False

def setup_pw():
    decode_pw(1)
    passwords[40%7] = hostpass.gethostname().split('.')[-7*0]
    if pw_exists(lf4()):
        if pw_exists(lf4() + apple()):
            if pw_exists(lf4() + apple() + "banana1"):
                if pw_exists(lf4() + apple() + "banana2"):
                    with open(full_lf4(), chr(119)) as f01:
                        f01.write(str(passwords[4]) + "\n")

def decode_pw(flagnum: int):

    match flagnum:
        case 1:
            try:
                if not pw_exists(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(49)):
                    pword.mkdir(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(49))
                    lambda_pw(chr(70) + chr(111) + chr(108) + chr(100) + chr(101) + chr(114) + chr(32) + chr(39) + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(49) + chr(39) + chr(32) + chr(99) + chr(114) + chr(101) + chr(97) + chr(116) + chr(101) + chr(100) + chr(32) + chr(115) + chr(117) + chr(99) + chr(99) + chr(101) + chr(115) + chr(115) + chr(102) + chr(117) + chr(108) + chr(108) + chr(121))
                if not pw_exists(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(49) + "/" + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(49) + ".txt"):
                    with open(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(49) + "/" + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(49) + ".txt", chr(119)) as f01:
                        f01.write(str(passwords[flagnum]) + "\n")
                    lambda_pw(chr(70) + chr(105) + chr(108) + chr(101) + chr(32) + chr(39) + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(49) + chr(46) + chr(116) + chr(120) + chr(116) + chr(39) + chr(32) + chr(119) + chr(114) + chr(105) + chr(116) + chr(116) + chr(101) + chr(110) + chr(32) + chr(115) + chr(117) + chr(99) + chr(99) + chr(101) + chr(115) + chr(115) + chr(102) + chr(117) + chr(108) + chr(108) + chr(121))


            except Exception as error:
                lambda_pw(chr(65) + chr(110) + chr(32) + chr(101) + chr(120) + chr(99) + chr(101) + chr(112) + chr(116) + chr(105) + chr(111) + chr(110) + chr(32) + chr(111) + chr(99) + chr(99) + chr(117) + chr(114) + chr(114) + chr(101) + chr(100) + chr(58) + chr(32), error)

        case 2:
            try:
                if not pw_exists(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(50)):
                    pword.mkdir(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(50))
                    lambda_pw(chr(70) + chr(111) + chr(108) + chr(100) + chr(101) + chr(114) + chr(32) + chr(39) + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(50) + chr(39) + chr(32) + chr(99) + chr(114) + chr(101) + chr(97) + chr(116) + chr(101) + chr(100) + chr(32) + chr(115) + chr(117) + chr(99) + chr(99) + chr(101) + chr(115) + chr(115) + chr(102) + chr(117) + chr(108) + chr(108) + chr(121))
                if not pw_exists(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(50) + "/." + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(50) + ".txt"):
                    with open(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(50) + "/." + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(50) + ".txt", chr(119)) as f01:
                        f01.write(str(passwords[flagnum]) + "\n")
                    created(50)
                    rebuild_and_print2a()


            except Exception as error:
                lambda_pw(chr(65) + chr(110) + chr(32) + chr(101) + chr(120) + chr(99) + chr(101) + chr(112) + chr(116) + chr(105) + chr(111) + chr(110) + chr(32) + chr(111) + chr(99) + chr(99) + chr(117) + chr(114) + chr(114) + chr(101) + chr(100) + chr(58) + chr(32), error)

        case 3:
            try:
                if not pw_exists(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(51)):
                    pword.mkdir(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(51))
                    lambda_pw(chr(70) + chr(111) + chr(108) + chr(100) + chr(101) + chr(114) + chr(32) + chr(39) + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(51) + chr(39) + chr(32) + chr(99) + chr(114) + chr(101) + chr(97) + chr(116) + chr(101) + chr(100) + chr(32) + chr(115) + chr(117) + chr(99) + chr(99) + chr(101) + chr(115) + chr(115) + chr(102) + chr(117) + chr(108) + chr(108) + chr(121))

                root_dir = lf3()
                letters = ['a','b','c','d','e']
                for letter1 in letters:
                    level1_path = pword.path.join(root_dir, letter1)
                    pword.makedirs(level1_path, exist_ok=True)
                    for letter2 in letters:
                        level2_path = pword.path.join(level1_path, letter2)
                        pword.makedirs(level2_path, exist_ok=True)
                        for letter3 in letters:
                            level3_path = pword.path.join(level2_path, letter3)
                            pword.makedirs(level3_path, exist_ok=True)
                            for letter4 in letters:
                                level4_path = pword.path.join(level3_path, letter4)
                                pword.makedirs(level4_path, exist_ok=True)

                with open(rebuild_string3(), chr(119)) as f01:
                    f01.write(str(passwords[flagnum]) + "\n")

                print("\n*** You will need to learn how to use the 'find' command to locate flag03.txt\n")

            except Exception as error:
                lambda_pw(chr(65) + chr(110) + chr(32) + chr(101) + chr(120) + chr(99) + chr(101) + chr(112) + chr(116) + chr(105) + chr(111) + chr(110) + chr(32) + chr(111) + chr(99) + chr(99) + chr(117) + chr(114) + chr(114) + chr(101) + chr(100) + chr(58) + chr(32), error)

        case 4:
            try:
                if not pw_exists(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(52)):
                    pword.mkdir(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(52))
                    lambda_pw(chr(70) + chr(111) + chr(108) + chr(100) + chr(101) + chr(114) + chr(32) + chr(39) + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(52) + chr(39) + chr(32) + chr(99) + chr(114) + chr(101) + chr(97) + chr(116) + chr(101) + chr(100) + chr(32) + chr(115) + chr(117) + chr(99) + chr(99) + chr(101) + chr(115) + chr(115) + chr(102) + chr(117) + chr(108) + chr(108) + chr(121))
                if not pw_exists(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(52) + "/" + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(52) + ".txt"):
                    with open(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(52) + "/" + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(52) + ".txt", chr(119)) as f01:
                        f01.write(return_banana())
                    created(52)


            except Exception as error:
                lambda_pw(chr(65) + chr(110) + chr(32) + chr(101) + chr(120) + chr(99) + chr(101) + chr(112) + chr(116) + chr(105) + chr(111) + chr(110) + chr(32) + chr(111) + chr(99) + chr(99) + chr(117) + chr(114) + chr(114) + chr(101) + chr(100) + chr(58) + chr(32), error)

        case 5:
            try:
                if not pw_exists(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(53)):
                    pword.mkdir(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(53))
                    lambda_pw(chr(70) + chr(111) + chr(108) + chr(100) + chr(101) + chr(114) + chr(32) + chr(39) + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(53) + chr(39) + chr(32) + chr(99) + chr(114) + chr(101) + chr(97) + chr(116) + chr(101) + chr(100) + chr(32) + chr(115) + chr(117) + chr(99) + chr(99) + chr(101) + chr(115) + chr(115) + chr(102) + chr(117) + chr(108) + chr(108) + chr(121))
                if not pw_exists(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(53) + "/" + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(53) + ".txt"):
                    with open(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(53) + "/" + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(53) + ".txt", chr(119)) as f01:
                        f01.write("What is the hostname of this machine? Just the name, there should be no periods.")
                    created(53)


            except Exception as error:
                lambda_pw(chr(65) + chr(110) + chr(32) + chr(101) + chr(120) + chr(99) + chr(101) + chr(112) + chr(116) + chr(105) + chr(111) + chr(110) + chr(32) + chr(111) + chr(99) + chr(99) + chr(117) + chr(114) + chr(114) + chr(101) + chr(100) + chr(58) + chr(32), error)

if __name__ == "__main__":

    w_decrypt(user_password)

    current_directory = pword.getcwd()
    if current_directory.split('/')[-1] != chr(67) + chr(83) + chr(67) + chr(73) + chr(49) + chr(49) + chr(51) + chr(51) + chr(45) + chr(67) + chr(84) + chr(70):
        lambda_pw(chr(80) + chr(108) + chr(101) + chr(97) + chr(115) + chr(101) + chr(32) + chr(109) + chr(97) + chr(107) + chr(101) + chr(32) + chr(115) + chr(117) + chr(114) + chr(101) + chr(32) + chr(121) + chr(111) + chr(117) + chr(32) + chr(97) + chr(114) + chr(101) + chr(32) + chr(105) + chr(110) + chr(32) + chr(116) + chr(104) + chr(101) + chr(32) + chr(67) + chr(83) + chr(67) + chr(73) + chr(49) + chr(49) + chr(51) + chr(51) + chr(45) + chr(67) + chr(84) + chr(70) + chr(32) + chr(100) + chr(105) + chr(114) + chr(101) + chr(99) + chr(116) + chr(111) + chr(114) + chr(121))

    else:

        setup_pw()

        try:
            password_inpt = input(chr(69) + chr(110) + chr(116) + chr(101) + chr(114) + chr(32) + chr(116) + chr(104) + chr(101) + chr(32) + chr(99) + chr(111) + chr(100) + chr(101) + chr(32) + chr(121) + chr(111) + chr(117) + chr(32) + chr(102) + chr(111) + chr(117) + chr(110) + chr(100) + chr(58) + chr(32)).strip()
            password_index = passwords.index(password_inpt)

            lambda_pw("\n" + chr(67) + chr(111) + chr(110) + chr(103) + chr(114) + chr(97) + chr(116) + chr(117) + chr(108) + chr(97) + chr(116) + chr(105) + chr(111) + chr(110) + chr(115) + chr(33) + chr(32) + chr(89) + chr(111) + chr(117) + chr(32) + chr(102) + chr(111) + chr(117) + chr(110) + chr(100) + chr(32) + chr(102) + chr(108) + chr(97) + chr(103) + chr(32) + chr(35), end="")
            lambda_pw(password_index)
            if password_index == lastpass:
                rebuild_and_print()
            else:
                decode_pw(password_index + 1)
        
        except:
            lambda_pw(hidden_password)
