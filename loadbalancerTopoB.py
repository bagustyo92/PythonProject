from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *
# from pyretic.examples.mac import *
from pyretic.modules.mac_learner import *

################################################
# Translate from
#   client -> public address : client -> server
#   server -> client : public address -> client
################################################
def translate(c, s, p):
    cp = match(srcip=c, dstip=p)
    sc = match(srcip=s, dstip=c)

    return ((cp >> modify(dstip=s)) +
            (sc >> modify(srcip=p)) +
            (~cp & ~sc))

class Tugas3(DynamicPolicy):
    def __init__(self, clients, servers, public_ip):
        super(Tugas3, self).__init__()

        print("Server addresses", servers)

        self.clients = clients
        self.servers = servers
        self.public_ip = public_ip

        #Variable distribusi request tiap server
        self.index = 0 #Untuk RR
        self.selector = 0 #Untuk WRR

        #Inisialisasi Nilai bobot Weighted Round Robin tiap server
        self.weightServer1 = 2
        self.weightServer2 = 1
        self.weightServer7 = 2
        self.weightServer8 = 1

        #Inisialisasi request counter Weighted Round Robin tiap server
        self.reqCounter1 = 0
        self.reqCounter2 = 0
        self.reqCounter7 = 0
        self.reqCounter8 = 0

        self.query = packets(1, ['srcip'])
        self.query.register_callback(self.update_policy)
        self.public_to_controller = (match(dstip=self.public_ip) >> self.query)
        self.lb_policy = None
        self.policy = self.public_to_controller

    def update_policy(self, pkt):

        client = pkt['srcip']
        dest = pkt['dstip']

        # Becareful not to redirect servers on themselves
        if client in self.servers: return

        #Pembagian distribusi request ke tiap server berdasarkan WRR
        server = self.rrModulus()
        p = translate(client, server, self.public_ip)

        if self.lb_policy:
            self.lb_policy = self.lb_policy >> p  # >> dinamis()
        else:
            self.lb_policy = p
        self.policy = self.lb_policy + self.public_to_controller  # + self.query

    def rrModulus(self):
        server = self.servers[self.index % len(self.servers)]
        self.index += 1
        print server
        return server

    def wrr(self):
        if(self.selector == 0):
            self.reqCounter1 += 1
            if(self.reqCounter1 < self.weightServer1):
                print self.servers[0]
                return self.servers[0]
            else:
                self.selector += 1
                self.reqCounter1 = 0
                print self.servers[0]
                return self.servers[0]
        if(self.selector == 1):
            self.reqCounter2 += 1
            if(self.reqCounter2 < self.weightServer2):
                print self.servers[1]
                return self.servers[1]
            else:
                self.selector += 1
                self.reqCounter2 = 0
                print self.servers[1]
                return self.servers[1]
        if (self.selector == 2):
            self.reqCounter7 += 1
            if (self.reqCounter7 < self.weightServer7):
                print self.servers[2]
                return self.servers[2]
            else:
                self.selector += 1
                self.reqCounter7 = 0
                print self.servers[2]
                return self.servers[2]
        if (self.selector == 3):
            self.reqCounter8 += 1
            if (self.reqCounter8 < self.weightServer8):
                print self.servers[3]
                return self.servers[3]
            else:
                self.selector = 0
                self.reqCounter8 = 0
                print self.servers[3]
                return self.servers[3]

def main():
    public_ip = IP("10.0.0.100")
    print("public ip address is %s." % public_ip)

    client_ips = [IP("10.0.0.3"), IP("10.0.0.4"), IP("10.0.0.5"), IP("10.0.0.6"), IP("10.0.0.9"), IP("10.0.0.10"), IP("10.0.0.11")]
    server_ips = [IP("10.0.0.1"),IP("10.0.0.2"), IP("10.0.0.7"), IP("10.0.0.8")]

    return (Tugas3(client_ips, server_ips, public_ip) >> flood())
