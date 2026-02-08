import socket
import threading
import time


class GameClient:
    def __init__(self, host="localhost", port=55400):
        self.host = host
        self.port = port
        self.conn = None
        self.snake1 = []
        self.snake2 = []
        self.snack = (0, 0)
        self.winner = 0
        self.direction = '2'

    def recive_messages(self):
        while True:
            try:
                message = self.conn.recv(1024)
            except ConnectionResetError:
                print("Utracono połączenie")
                break
            if not message:
                print("Utracono połączenie")
                break
            self.winner = message[0]         # pierwszy bajt
            len_snake1 = message[1]     # drugi bajt
            snake1 = []
            offset = 2  # zaczynamy po winner i len_snake1
            for i in range(len_snake1):
                x = message[offset]
                y = message[offset + 1]
                snake1.append((x, y))
                offset += 2
            len_snake2 = message[offset]
            offset += 1
            snake2 = []
            for i in range(len_snake2):
                x = message[offset]
                y = message[offset + 1]
                snake2.append((x, y))
                offset += 2
            self.snake1 = snake1
            self.snake2 = snake2
            self.snack = (message[offset], message[offset + 1])

            offset += 2
            print(f"Winner: {self.winner}")
            print(f"Snake1: {self.snake1}")
            print(f"Snake2: {self.snake2}")
            print(f"Snack: {self.snack}")

    def send_messages(self):
        last_direction = self.direction
        while True:
            if self.direction != last_direction:
                self.conn.send(self.direction.encode())
                last_direction = self.direction
            time.sleep(1/9)  # dodajemy małe opóźnienie, aby nie wysyłać zbyt wielu wiadomości na raz

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
            self.conn = conn
            self.conn.connect((self.host, self.port))
            receiver = threading.Thread(target=self.recive_messages, daemon=True)
            receiver.start()
            self.send_messages()

  

if __name__ == "__main__":
    client = GameClient()
    client.start()