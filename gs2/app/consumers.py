# Consumer Topic

from channels.consumer import SyncConsumer,AsyncConsumer

class MySyncConsumer(SyncConsumer):

    # This hander is called when client initially open a connection and is about to finished the websocket
    def websocket_connect(self,event):
        print("Websocket connected...")

    # This handler is called when data received from client
    def websocket_receive(self,event):
        print("Messaged Received...")

    # this handler is called when either connection to the client is lost
    # , either from the client closing the connection, the server closing 
    # the connection or loss of the socket
    def websocket_disconnect(self,event):
        print("Websocket Disconnected...")


class MyAsyncConsumer(AsyncConsumer):

    # This hander is called when client initially open a connection and is about to finished the websocket
    async def websocket_connect(self,event):
        print("Websocket connected...")

    # This handler is called when data received from client
    async def websocket_receive(self,event):
        print("Messaged Received...")

    # this handler is called when either connection to the client is lost
    # , either from the client closing the connection, the server closing 
    # the connection or loss of the socket
    async def websocket_disconnect(self,event):
        print("Websocket Disconnected...")