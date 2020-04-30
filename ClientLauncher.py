__author__ = 'Tibbers'
import sys
from Tkinter import Tk
from Client import Client

if __name__ == "__main__":
	try:
		serverAddr = sys.argv[1]
		serverPort = sys.argv[2]
		rtpPort = sys.argv[3]
		fileName = sys.argv[4]
		#print(serverAddr)
		print(sys.argv[2])
		#print (rtpPort)
	except:
		print "[Usage: ClientLauncher.py Server_name Server_port RTP_port Video_file]\n"

	root = Tk()
	# Create a new client
	#print(serverAddr)
	#print(ServerPort)
	#print (rtpPort)
	#app = Client(root, serverAddr, serverPort, rtpPort, fileName)
	app = Client(root,serverAddr,serverPort,rtpPort,fileName)
	app.master.title("RTPClient")
	#app.master.title("RTPClient")
	root.mainloop()
