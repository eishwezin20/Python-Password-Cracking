import os

os.system("rm -rf secret")

try:
   pass_file = open("10-million-password-list-top-1000000.txt", "r")
except:
   print("Password file not opened")
   quit()

for password in pass_file:
    password = password.replace("\n","")
    cmd = "unzip -P " + password + " secret.zip"
    print(cmd)

    err_code = os.system(cmd)
    print(err_code)

    if err_code != 20992 and err_code != 0:
        os.system("rm -rf secret")
        #input("next")

    if err_code == 0:
        print(f"ZIP password is {password}")
        exit()
