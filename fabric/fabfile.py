from fabric.api import *
def greeting(msg):
    print(f'Hi {msg}')

def system_info():
    local('df -h')

    local('free -m')

    local('uptime')


def remote_exec():
    run('df -h')

    run('free -m')

    run('uptime')

    sudo("yum update -y")

def web_setup(WEBURL, DIRNAME):

   local("sudo apt install zip unzip -y")


   print("Installing dependencies")
   
   sudo("yum install httpd wget zip unzip -y")


   print("Start & enable service.")

   sudo("systemctl start httpd")
   sudo("systemctl enable httpd")


   print("Downloading and pushing website to webservers.")
   import os

   if os.path.isdir(DIRNAME): 
        local(("wget -O website.zip %s") % WEBURL)
        local("unzip -o website.zip")
   

   with lcd(DIRNAME):
        local("zip -r tooplate.zip * ")
        put("tooplate.zip", "/var/www/html/", use_sudo=True)

   with cd("/var/www/html/"):
        sudo("unzip -o tooplate.zip")

   sudo("systemctl restart httpd")

   print("Website setup is done.")
