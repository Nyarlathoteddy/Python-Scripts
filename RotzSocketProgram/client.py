import socket

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    sending = True
    client.connect((HOST,PORT))
    while sending:
        data = client.recv(1024)
        data = data.decode("utf-8")
        print(data)
        message = input("Answer:")
        if message == "quit":
            client.close()
            break
        while message == "":
            print("Please enter an answer.")
            message = input("Answer:")
        else:
            client.send(message.encode("utf-8"))
            print(data)
            if data == "quit":
                sending = False