from functions import tryconnect, connectpassword
from paramiko import SSHClient, AutoAddPolicy, RSAKey
from scp import SCPClient
from os import path
import io
import sys

user = "root"
keypath = "/root/.ssh/root"
remotehost = "192.168.58.49"
defaultpassword = "root"
ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy)

print("Welcome to the ssh master")
remotehost = input("Give your remote server IP (192.168.58.49): ") or remotehost
defaultpassword = input("Give the default password (root): ") or defaultpassword
user = input("Give the default username (root): ") or user
keypath = input("Give the path for the key (/root/.ssh/root): ") or keypath
localpath = input("Give the path for the local file to copy (key path)") or keypath
extpath = input("Give the path where you want to put the file (key path)") or keypath
print("Will start the ssh connection")

if path.exists(keypath):
    key = RSAKey.from_private_key_file(keypath)
    i = tryconnect(ssh, remotehost, user, key, defaultpassword)
    print(i)
    if i == 0:
        sys.exit()
else:
    i = connectpassword(ssh, remotehost, user, defaultpassword)
    print(i)
    if i == 0:
        sys.exit()
print("hoalaaa")
if path.exists(localpath):
    print("holaaa")
    scp = SCPClient(ssh.get_transport())
    scp.put(localpath, extpath)
    ssh.exec_command("cat extpath")
    scp.close()

ssh.close()
