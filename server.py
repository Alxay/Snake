import socket
import threading
import asyncio
import struct
from game import Game
import sys


clients = []
running = True
TICKRATE = 9


def sendData(snake1,snake2,snack,winner):
    print("Sending data to clients")
    print(f"Snake1: {snake1} Snake2: {snake2} Snack: {snack} Winner: {winner}")
    data = bytearray()
    data.append(winner)
    data.append(len(snake1))  # długość
    for x, y in snake1:
        data += struct.pack("!BB", x, y)
    data.append(len(snake2))  # długość
    for x, y in snake2:
        data += struct.pack("!BB", x, y)
    data += struct.pack("!BB", snack[0], snack[1])
    for client in clients:
        client.send(data)

    if winner != 0:
        print(f"Winner: {winner}")
        off()
    

game = Game(sendData)
# def pack_snake(snake):
#     data = bytearray()
#     data.append(len(snake))  # długość
#     for x, y in snake:
#         data += struct.pack("!BB", x, y)
#     return data

def off():
    for client in clients:
        client.close()
    print("Shutting down server")
    global running
    running = False  
    sys.exit(0)
    

def handle_client(conn):
    print(conn)
    id  = len(clients) - 1
    print(f"Client {id} connected")
    message = 2
    while running:
        try:
            raw = conn.recv(1)
        except (ConnectionResetError, ConnectionAbortedError):
            print(f"Client {id} disconnected (reset)")
            break
        if not raw:
            print(f"Client {id} disconnected")
            break
        data = raw.decode()
        if data not in ['1','2','3','4']:
            print(f"Received invalid data from client {id}: {data}")
        else:
            message = data
        if id == 0:
            print(f"Zmieniam kierunek na gracza nr 1: {message}")
            game.direction = int(message)
        else:
            print(f"Zmieniam kierunek na gracza nr 2: {message}")
            game.direction2 = int(message)
    clients.remove(conn)
    conn.close()

def start_game_loop():
    asyncio.run(game.game_loop())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(('localhost',55400))
    server.listen(2)
    server.settimeout(1) 
    while running:
        try:
            client,adress = server.accept()
            connected_client = threading.Thread(target=handle_client,daemon=True,args=(client,))
            connected_client.start()
            clients.append(client)
            if len(clients) == 2:
                print("Starting game loop")
                threading.Thread(target=start_game_loop, daemon=True).start()
        except socket.timeout:
            continue  # co 1 sekundę sprawdzamy flagę `running`
            
        
            
            






