__author__ = 'Tibbers'
import sys, socket

from ServerWorker import ServerWorker

class Server:

	def main(self):
		try:
			SERVER_PORT = int(sys.argv[1])
		except:
			print "[Usage: Server.py Server_port]\n"
		rtspSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		rtspSocket.bind(('172.31.16.7', SERVER_PORT))
		rtspSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		print "RTSP Listing incoming request..."
		rtspSocket.listen(20)
		rtpSocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)#change here
		rtpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		rtpSocket.bind(('172.31.16.7', 17023))
		rtpSocket.listen(20)
		# Receive client info (address,port) through RTSP/TCP session
		while True:
			clientInfo = {}
			clientInfo['rtspSocket'] = rtspSocket.accept()   # this accept {SockID,tuple object},tuple object = {clinet_addr,intNum}!!!
			clientInfo['rtpSocket']  = rtpSocket.accept()
			print('We have accepted a connection from 1 ', clientInfo['rtspSocket'][1])
        		print('  Socket name:', clientInfo['rtspSocket'][0].getsockname())
        		print('  Socket peer:', clientInfo['rtspSocket'][0].getpeername())
        		print('We have accepted a connection from', clientInfo['rtpSocket'][1])
	        	print('  Socket name:', clientInfo['rtpSocket'][0].getsockname())
	        	print('  Socket peer:', clientInfo['rtpSocket'][0].getpeername())
	        	ServerWorker(clientInfo).run()


# Program Start Point
if __name__ == "__main__":
	(Server()).main()