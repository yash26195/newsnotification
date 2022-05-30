import socket
import sys
import random

from _thread import *
from threading import Timer

userList = []
newstopics = ['World','Politics','Sports','Technology','Stocks']
topics = ['World','Politics','Sports']
subscriptions = {}
events = { 'World' : ['Flights cancelled on busy Memorial Day', 'US stop soaring oil and gas prices', 'Pope announces 21 new Cardinals'],
    'Politics' : ['Billionaire Attacking Elon Musk'],
    'Sports' : ['Boston will reach NBA Finals','Sergio Perez win Monaco Grand Prix']
}

generatedEvents = dict()
flags = dict()

def threadedClient(connection, data):
    while True:
        flags[data] = 0
        subscribe(data)
        subscriptionInfo = 'Your subscriptions are : ' + str(subscriptions[data])
        connection.send(subscriptionInfo.encode())

        while True:
            if flags[data]==1:
                notify(connection,data)
    connection.close()

def threadedServerSender(connection, data):
    while True:
        flags[data] = 0
        subscriptions[data] = topics
        subscriptionInfo = 'Your subscriptions are : ' + str(subscriptions[data])
        connection.send(subscriptionInfo.encode())
        
        while True:
            if flags[data]==1:
                notify(connection,data)
    connection.close()

def threadedServerReceiver(connection, data):
    while True:
        serverData = connection.recv(2048).decode()
        m = serverData.split('-')
        if len(m)==2:
            topic = m[0]
            event = m[1]
            publish(topic,event,0)
    connection.close()

def subscribe(name):
    subscriptions[name] = ['World']


def eventGenerator():
    
    topic = random.choice(topics)
    msgList = events[topic]
    event = msgList[random.choice(list(range(1,len(msgList))))]
    
    publish(topic,event,1)


def publish(topic,event,indicator):
    
    event = topic + ' - ' + event
    
    if indicator == 1:
        for name, topics in subscriptions.items() :
            if topic in topics:
                if name in generatedEvents.keys():
                    generatedEvents[name].append(event)
                else:
                    generatedEvents.setdefault(name, []).append(event)
                flags[name] = 1

    else:
        for name, topics in subscriptions.items() :
            if name in userList: # only for clients
                if topic in topics:
                    if name in generatedEvents.keys():
                        generatedEvents[name].append(event)
                    else:
                        generatedEvents.setdefault(name, []).append(event)
                    flags[name] = 1

    t = Timer(random.choice(list(range(20,26))), eventGenerator)
    t.start()

                 
def notify(connection,name):
    if name in generatedEvents.keys():
        for msg in generatedEvents[name]:
            msg = msg  + str("\n")
            connection.send(msg.encode())
        del generatedEvents[name]
        flags[name] = 0

def Main():
    
    host = "" 
    port = 5040
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host,port))
    print("Socket is bind to the port :", port)
    s.listen(5)
    print("Socket is now listening for new connection ...")
    
    t = Timer(random.choice(list(range(20,26))), eventGenerator)
    t.start()
    
    while True:
        
        connection, addr = s.accept() 
        print('Connected to :', addr[0], ':', addr[1])
        data = connection.recv(2048).decode()

        if data:
            print("Welcome ", data)
        
        l = data.split('-')
        
        if l[0]=='c':
            userList.append(l[1])
            start_new_thread(threadedClient, (connection,l[1]))
        if l[0]=='s':
            start_new_thread(threadedServerSender, (connection,l[1]))
            start_new_thread(threadedServerReceiver, (connection,l[1]))

    s.close()

if __name__ == '__main__':
    Main() 
