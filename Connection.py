import socket
import time


class Connection:
    def __init__(self, hostname: str, port: int = 2000) -> None:
        self.buffer: list[int] = []
        self.hostname = hostname
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self) -> bool:
        try:
            print("connecting to %s:%d..." % (self.hostname, self.port))
            self.socket.connect((self.hostname, self.port))
            print("connection established")
            return True
        except:
            print("connection failed!")
            return False

    def disconnect(self) -> bool:
        try:
            print("disconnecting...")
            self.socket.close()
            print("connection terminated")
            return True
        except:
            print("connection can't be terminated!")
            return False

    def send(self, order: str) -> None:
        self.socket.send(order.encode())

    def receive(self, timeout: float = 1.0) -> str:
        startTime = time.time()
        while True:
            inputBytes = self.socket.recv(1)
            for byte in inputBytes:
                if byte == 10:  # \n
                    message = bytearray(self.buffer).decode()
                    self.buffer.clear()
                    return message
                self.buffer.append(byte)
            if time.time() - startTime >= timeout:
                return ""

    def giveSocket(self) -> socket.socket:
        return self.socket

    def giveHostname(self) -> str:
        return self.hostname

    def givePort(self) -> int:
        return self.port