#from twisted.internet import stdio
from twisted.protocols import basic
from twisted.internet import reactor

from twisted.internet import reactor, protocol

# Protocol untuk pengiriman sama penerimaan data dari server
class EchoClient(protocol.Protocol):

	def connectionMade(self):
		input = raw_input("Masukkan pesan yang akan dikirim : ")
		self.transport.write(input)
		
	def dataReceived(self, data):
		print "Server said:", data
		input = raw_input("Masukkan pesan yang akan dikirim : ")
		self.send_message(input)
		
	def send_message(self, input) :
		self.transport.write(input)
	
class EchoFactory(protocol.ClientFactory):
	client = None

	def buildProtocol(self, addr):
		self.client = EchoClient()
		return self.client


def main():
	factory = EchoFactory()
	# Koneksi ke TCP server
	reactor.connectTCP("localhost", 8002, factory)
	# Koneksi ke console untuk dapatkan input dari keyboard
	reactor.run()

if __name__ == '__main__':
	main()