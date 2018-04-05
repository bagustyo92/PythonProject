#Import
from twisted.internet import reactor, protocol

# Protocol
class Echo(protocol.Protocol):
	"""This is just about the simplest possible protocol"""
	
	# Fungsi callback ketika ada pesan masuk
	def dataReceived(self, data):
		self.transport.write("OK "+data)
		print "masuk data receive"

#Factory
class EchoFactory(protocol.Factory):
	def buildProtocol(self, addr):
		return Echo()
		print "masuk echo factory"

reactor.listenTCP(8002, EchoFactory())
reactor.run()