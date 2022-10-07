from functions import tryconnect, connectpassword
from paramiko import SSHClient, AutoAddPolicy, RSAKey
from scp import SCPClient
from os import path
import io
import sys

user = "frodo"
keypath = "/home/frodo/.ssh/frodo"
remotehost = "192.168.1.134"
defaultpassword = "bolson"
ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy)

print("Welcome to the ssh master")
remotehost = input("Give your remote server IP (192.168.1.134): ") or remotehost
defaultpassword = input("Give the default password (bolson): ") or defaultpassword
user = input("Give the default username (frodo): ") or user
keypath = input("Give the path for the key (/home/frodo/.ssh/frodo): ") or keypath
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
print("holaaa")
if path.exists(localpath):
    print("holaaa")
    scp = SCPClient(ssh.get_transport())
    scp.put(localpath, extpath)
    ssh.exec_command("cat extpath")
    scp.close()

ssh.close()
