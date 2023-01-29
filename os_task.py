#!/usr/bin/python3.8
import os

if os.path.isfile("."):
    print("CCC")

users = [ "anhgrews", "beta", "gama" ]
# os.system("ls -l")
# os.system("mkdir tmp")

# os.system("ls -l")
# print(exit_code)

for user in users:
    exit_code = os.system(f'id {user}')
    if exit_code == 0:
        print("OKE")
    else:
        os.system(f'useradd {user}')
        print(f"Adding user {user}")

os.system("groupadd science")

if not os.path.isdir("./sciences"):
    os.mkdir("./sciences")
    os.system("chown :science ./sciences")
    os.system("chmod 770 ./sciences")

for user in users:
    os.system(f'usermod -aG science {user}')
    print(f"Adding user {user} to sciences group")

for user in users:
    os.system(f'sudo userdel -rf {user}')
    print(f"Deleting user {user} to sciences group")

os.system("sudo groupdel science")
os.rmdir("./tmp/")