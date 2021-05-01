import socket
from electionServer import CreateElection


class CreateSocket:
    def __init__(self, sock=None) -> None:
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.election = CreateElection()
        self.election.set_candidates(eduardo='22', juninho_capixaba='33')

    def server_socket(self) -> None:
        self.sock.bind(('localhost', 50005))
        self.sock.listen(10)

    def run_socket(self) -> None:
        self.server_socket()
        while True:
            (connection, address) = self.sock.accept()
            print(f'Connection successful on {address}')
            data: bytes = connection.recv(1024)

            if data.decode() == '22':
                self.election.vote_for('22')
                connection.sendall(str.encode('OK'))

            if data.decode() == '33':
                self.election.vote_for('33')
                connection.sendall(str.encode('OK'))

            if data.decode() == 'show':
                connection.sendall(str.encode(self.election.show()))

            if data.decode() == 'show_info':
                connection.sendall(str.encode(self.election.show_info()))

            if not data:
                print(f'Connection Closed.')
                connection.close()
                break

            else:
                connection.sendall(str.encode("I dont found a candidate with this number!"))

            connection.sendall(data)
            connection.close()
