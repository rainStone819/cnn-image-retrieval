# -*- coding: UTF-8 -*-

import socket
import socketserver
import json
from collections import OrderedDict
from index import Searcher

searcher = Searcher()
searcher.loadIndex()
json_encoder=json.JSONEncoder()

def search(query_img):
    similar_imgs, distances=searcher.search(query_img)
    result=''
    for i in xrange(len(similar_imgs)):
        result += str(similar_imgs[i]) + '\t' + str(distances[i]) + '\n'
    return result

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        buffersize=1024
        while True:
            ret_bytes = conn.recv(buffersize)
            ret_str = str(ret_bytes)
            print "client adress: %s, request data: %s" % (self.client_address,ret_str)
            # the absolute path of query image
            ret_str = "/htdocs/image-retrieval-UI/query_images/" + ret_str
            response=search(ret_str)
            conn.send(response)
            break

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 15809
    print "open the socket server, host: %s, port: %s" % (host,port)
    server = socketserver.ThreadingTCPServer((host,port),Myserver)
    server.serve_forever()