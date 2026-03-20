
#not using

import socket
import json
from _thread import *
from playerClass import *
import game


class Network:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.90.78.56"
        self.port = 50101
        self.addr = (self.server, self.port)
        try:
            self.socket.connect(self.addr)
            print("Connection established")
            start_new_thread(self.receive_message())
            print("thread created")
        except error as e:
            print(error)
            quit()

    def process_command(self, cmd, socket):

        if cmd["Command"] == "Start":
            game()
        if cmd["Command"] == "MOVE":
            self.move_others(cmd)

    def send(self, data):
        try:
            if self.socket != None:
                self.socket.send(json.dumps(data).encode())

        except socket.error as e:
            print(e)

    def receive_message(self):
        while True:
            response = self.socket.recv(2048)
            if response:
                cmd = json.loads(response.decode())
                print(cmd)
                self.process_command(cmd, self.socket)

    def move_others(self, cmd):
        # p2.rect.x = cmd["X"]
        # p2.rect.y = cmd["Y"]
        pass
