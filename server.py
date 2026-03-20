import socket
from _thread import *
import json
import sys

SERVER = "192.168.0.21"  # this wont work at college, only home
SERVER = "127.0.0.1"  # this will work wherever - so long as the client and server are on the same machine
PORT = 50103



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((SERVER, PORT))
except:
    print("error")

s.listen(6)
print("Waiting for a connection, SERVER started")

commands = []
def process_command(connection, command, client_list):

    """if command["Command"] == "MOVE":
        #x = command["X"]
        #y = command["Y"]
        direction = command["DIR"]
        for client in client_list:
            if client != connection:
                #cmd = {"Command": "MOVE", "X": x, "Y": y, "DIRECTION": direction}
                cmd = {"Command": "MOVE", "DIR": direction}
                client.send(json.dumps(cmd).encode())
                print("SENDING", cmd)
    if command["Command"] == "ROTATE":
        angle = command["ANGLE"]
        for client in client_list:
            if client != connection:
                #cmd = {"Command": "MOVE", "X": x, "Y": y, "DIRECTION": direction}
                cmd = {"Command":"ROTATE", "ANGLE": angle}
                client.send(json.dumps(cmd).encode())
                print("SENDING", cmd)"""
    for client in client_list:
        if client != connection:
            if command["Command"] == "MOVE":
                # x = command["X"]
                # y = command["Y"]
                direction = command["DIR"]
                player_number = command["PLAYER_NUMBER"]
                cmd = {"Command": "MOVE", "DIR": direction, "PLAYER_NUMBER": player_number}
                commands.append(cmd)
            if command["Command"] == "ROTATE":
                angle = command["ANGLE"]
                player_number = command["PLAYER_NUMBER"]
                cmd = {"Command": "ROTATE", "ANGLE": angle, "PLAYER_NUMBER": player_number}
                commands.append(cmd)
            if command["Command"] == "SHOOT":
                angle = command["ANGLE"]
                player_number = command["PLAYER_NUMBER"]
                cmd = {"Command": "SHOOT", "ANGLE": angle, "PLAYER_NUMBER": player_number}
                commands.append(cmd)
            for command in commands:
                client.send(json.dumps(command).encode())
                print("SENDING", command)
                commands.remove(command)



def setup_game(client_list):
    for client in client_list:
        cmd = {"Command": "Start", "client_id": client_list.index(client)}
        client.send(json.dumps(cmd).encode())


def threaded_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(1024 * 16)
            reply = data.decode("utf-8")
            reply1 = json.loads(reply)
            if not data:
                print("Client:", conn, "Disconnected")
                break
            else:
                print("Received: ", reply)
                process_command(conn, reply1, client_list)

        except error as e:
            print(e)
    print("Lost connection")
    conn.close()


client_list = []

while True:
    conn, addr = s.accept()
    print("Connected to client:", addr)
    client_list.append(conn)

    start_new_thread(threaded_client, (conn,))
    if len(client_list) == 6:
        setup_game(client_list)
