import socket
import subprocess
import threading
import socket


HOST = ""
PORT = 6666


def server(conn,address):
    try:
        print("Got connection " + address)
        while True:
            data = conn.recv(1024)
            if data == "":
                print("Socket closed remotely")
                break

            conn.sendall(data)

    except Exception as e:
        raise
    finally:
        conn.close()



if __name__ == "__main__":

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        try:
            while True:

                conn, address = s.accept()
                process = multiprocessing.Process(target=handle, args=(conn, address))
                process.daemon = True
                process.start()
        except Exception as e:
            raise
        finally:

            for thread in threading.enumerate():

                thread.terminate()

