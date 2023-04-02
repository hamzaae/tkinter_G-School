import mysql.connector
import socket
import hashlib
import threading

### DB section
"""mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password123",
  database="g_school"
)
mycursor = mydb.cursor()

user1id = 1
user1name = "admin"
user1password = hashlib.sha256("password123".encode()).hexdigest()
user1type = "admin"
user1mail = "motassimhamza99@gmail.com"
user1phone = "0688415630"

mycursor.execute("INSERT INTO users (id,username,passwordd,type,email,phone) values(%s,%s,%s,%s,%s,%s)",
                 (user1id,user1name,user1password,user1type,user1mail,user1phone))
mydb.commit()"""
# client
"""client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost", 9999))

        message = client.recv(1024).decode()
        client.send(input(message).encode())
        message = client.recv(1024).decode()
        client.send(input(message).encode())
        print(client.recv(1024).decode())"""


# Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost",9999))
server.listen()

def handle_connection(c):
    c.send("Username: ".encode())
    username = c.recv(1024).decode()
    c.send("Password: ".encode())
    password = c.recv(1024)
    password = hashlib.sha256(password).hexdigest()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password123",
        database="g_school"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users WHERE username = %s AND passwordd = %s",
                           (username,password))
    if mycursor.fetchall():
        c.send("Login successful!".encode())
    else:
        c.send("Login failed!".encode())

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client, )).start()




