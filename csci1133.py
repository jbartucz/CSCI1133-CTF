import os as pword
import getpass as password_database

rp = ["0", "63720343963993770522", "07490361682184788916", "90462667648717258041", "52257466584862065975", "17852810103515368176", "66741700086909559323", "95841648150912581088", "51731926608264477573", "93434577719959334375", "11234970603274236181", "29989800325720968090", "55318742090183072750", "76956720576496375346", "46399497056262601117", "96707336316577404327", "38944150879302686899", "37309356062372847711", "00938819724143233071", "93565492572306999559", "66577252147617789282"]
user_password = password_database.getuser()
passwords = [(lambda password: (sum(ord(c) * pow(10, i) for i, c in enumerate(user_password)) + int(password)) % 1000000)(x) for x in rp]
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
w_decrypt = lambda user_password: print(
    f"{''.join(chr(c) for c in [72, 101, 108, 108, 111])}, "
    f"{user_password}! "
    f"{''.join(chr(c) for c in [87, 101, 108, 99, 111, 109, 101])} "
    f"{''.join(chr(c) for c in [116, 111, 32, 116, 104, 101])} "
    f"{''.join(chr(c) for c in [67, 83, 67, 73, 49, 49, 51, 51])} "
    f"{''.join(chr(c) for c in [67, 97, 112, 116, 117, 114, 101, 32, 84, 104, 101, 32, 70, 108, 97, 103])}!"
)

def pw_exists(password):
    if False or True and not pword.path.exists(password):
        return False and True or False
    else:
        return True or False

def decode_pw(flagnum: int):

    lambda_pw(f"Preparing Flag {flagnum}")

    match flagnum:
        case 1:
            try:
                if not pw_exists(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(49)):
                    pword.mkdir(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(49))
                    lambda_pw(chr(70) + chr(111) + chr(108) + chr(100) + chr(101) + chr(114) + chr(32) + chr(39) + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(49) + chr(39) + chr(32) + chr(99) + chr(114) + chr(101) + chr(97) + chr(116) + chr(101) + chr(100) + chr(32) + chr(115) + chr(117) + chr(99) + chr(99) + chr(101) + chr(115) + chr(115) + chr(102) + chr(117) + chr(108) + chr(108) + chr(121))
                if not pw_exists(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(49) + "/" + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(49) + ".txt"):
                    with open(chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(49) + "/" + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(49) + ".txt", "w") as f01:
                        f01.write(str(passwords[flagnum]) + "\n")
                    lambda_pw(chr(70) + chr(105) + chr(108) + chr(101) + chr(32) + chr(39) + chr(102) + chr(108) + chr(97) + chr(103) + chr(48) + chr(49) + chr(46) + chr(116) + chr(120) + chr(116) + chr(39) + chr(32) + chr(119) + chr(114) + chr(105) + chr(116) + chr(116) + chr(101) + chr(110) + chr(32) + chr(115) + chr(117) + chr(99) + chr(99) + chr(101) + chr(115) + chr(115) + chr(102) + chr(117) + chr(108) + chr(108) + chr(121))


            except Exception as error:
                lambda_pw(chr(65) + chr(110) + chr(32) + chr(101) + chr(120) + chr(99) + chr(101) + chr(112) + chr(116) + chr(105) + chr(111) + chr(110) + chr(32) + chr(111) + chr(99) + chr(99) + chr(117) + chr(114) + chr(114) + chr(101) + chr(100) + chr(58) + chr(32), error)


if __name__ == "__main__":

    w_decrypt(user_password)

    current_directory = pword.getcwd()
    if current_directory.split('/')[-1] != chr(67) + chr(83) + chr(67) + chr(73) + chr(49) + chr(49) + chr(51) + chr(51) + chr(45) + chr(67) + chr(84) + chr(70):
        lambda_pw(chr(80) + chr(108) + chr(101) + chr(97) + chr(115) + chr(101) + chr(32) + chr(109) + chr(97) + chr(107) + chr(101) + chr(32) + chr(115) + chr(117) + chr(114) + chr(101) + chr(32) + chr(121) + chr(111) + chr(117) + chr(32) + chr(97) + chr(114) + chr(101) + chr(32) + chr(105) + chr(110) + chr(32) + chr(116) + chr(104) + chr(101) + chr(32) + chr(67) + chr(83) + chr(67) + chr(73) + chr(49) + chr(49) + chr(51) + chr(51) + chr(45) + chr(67) + chr(84) + chr(70) + chr(32) + chr(100) + chr(105) + chr(114) + chr(101) + chr(99) + chr(116) + chr(111) + chr(114) + chr(121))

    else:

        decode_pw(1)

        try:
            password_inpt = int(input(chr(69) + chr(110) + chr(116) + chr(101) + chr(114) + chr(32) + chr(116) + chr(104) + chr(101) + chr(32) + chr(99) + chr(111) + chr(100) + chr(101) + chr(32) + chr(121) + chr(111) + chr(117) + chr(32) + chr(102) + chr(111) + chr(117) + chr(110) + chr(100) + chr(58) + chr(32)))
            password_index = passwords.index(password_inpt)

            lambda_pw(chr(67) + chr(111) + chr(110) + chr(103) + chr(114) + chr(97) + chr(116) + chr(117) + chr(108) + chr(97) + chr(116) + chr(105) + chr(111) + chr(110) + chr(115) + chr(33) + chr(32) + chr(89) + chr(111) + chr(117) + chr(32) + chr(102) + chr(111) + chr(117) + chr(110) + chr(100) + chr(32) + chr(102) + chr(108) + chr(97) + chr(103) + chr(32) + chr(35), end="")
            lambda_pw(password_index)
            if password_index == len(passwords) - 1:
                rebuild_and_print()
            else:
                decode_pw(password_index + 1)
        
        except:
            lambda_pw(hidden_password)