from channels.consumer import SyncConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("Web Socket Connect")
        
    def websocket_receive(self,event):
        print("Websocket Received..")

    def websocket_disconnect(self,event):
        print("Websocket Disconnect")