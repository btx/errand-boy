import logging
import socket

from errand_boy.transports.base import BaseTransport
from errand_boy.transports.unixsocket import UNIXSocketTransport

logger = logging.getLogger(__name__)


class TcpSocketTransport(UNIXSocketTransport):
    def __init__(self, adress_ip=None, address_port=8888, listen_backlog=5, **kwargs):
        BaseTransport.__init__(self)

        self.adress_ip = adress_ip if adress_ip is not None else socket.gethostname()
        self.address_port = address_port
        self.listen_backlog = listen_backlog

    def server_get_connection(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        serversocket.bind((self.adress_ip, self.address_port))
        serversocket.listen(self.listen_backlog)

        return serversocket

    def client_get_connection(self):
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        clientsocket.connect((self.adress_ip, self.address_port))

        return clientsocket
