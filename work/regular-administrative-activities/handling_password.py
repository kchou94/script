import sys
import paramiko
import time

ip_address = "192.168.10.76"
username = "vagrant"
password = "vagrant"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.load_system_host_keys()
ssh_client.connect(hostname=ip_address, username=username, password=password)

print("Successful connection", ip_address)

ssh_client.invoke_shell()
remote_connection = ssh_client.exec_command('cd Desktop; mkdir test\n')
remote_connection = ssh_client.exec_command('mkdir test_folder\n')

ssh_client.close()
