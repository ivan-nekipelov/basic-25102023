import socketserver

class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        data, conn = self.request
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        # just send back the same data, but upper-cased
        conn.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 8842

    # Create the server, binding to localhost on port 8842
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()