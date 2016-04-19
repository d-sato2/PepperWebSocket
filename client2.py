from websocket import create_connection
ws = create_connection("wss://afternoon-bastion-99962.herokuapp.com/receive")
print "Receiving..."
for i in range(10):
            result = ws.recv()
            print "Received '%s'" % result
ws.close()
