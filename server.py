import socket
from _thread import *
from board import Board
import pickle
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "localhost"
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen()
print("[START] Waiting for a connection")

connections = 0

games = {0:Board(8, 8)}

spectartor_ids = [] 
specs = 0

def read_specs():
    global spectartor_ids

    spectartor_ids = []
    try: 
        with open ("spec.txt", "r") as f:
            for line in f:
                spectartor_ids.append(line.strip())
    except:
        print("[ERROR] No specs.txt file found, creating one...")
        open("specs.txt", "w")

def threaded_client(conn,game,spec = False):
    global pos, games, currentId, connections, specs

    if not spec:
        name = None
        bo = games[game]

        if connections % 2 == 0:
            currentId = "w"
        else:
            currentId = "b"

        bo.start_user = currentId

        # Pickle the object and send it to the server
        data_string = pickle.dumps(bo)

        if currentId == "b":
            bo.ready = True
            bo.startTime = time.time()

        conn.send(data_string)
        connections += 1

        while True:
            if game not in games:
                break
            
            try:
                d = conn.recv(8192 * 3)
                data = d.decode("utf-8")
                if not d:
                    break
                else:
                    if data.count("select") > 0:
                        all = data.split(" ")
                        col = int(all[1])
                        row = int(all[2])
                        color = all[3]
                        bo.select(col, row, color)

                    if data == "winner b":
                        bo.winner = "b"
                        print("[GAME] Player b won in game", game)
                    if data == "winner w":
                        bo.winner = "w"
                        print("[GAME] Player w won in game", game)

                    if data == "update moves":
                        bo.update_moves()

                    if data.count("name") == 1:
                        name = data.split(" ")[1]
                        if currentId == "b":
                            bo.p2Name = name
                        elif currentId == "w":
                            bo.p1Name = name