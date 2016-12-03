#!/usr/bin/env python

import argparse
import json
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class Database:

  def __init__(self):
        self.db = {}
        self.count = 0

  def add_note(self, note):
    self.count += 1
    self.db[self.count] = {'id': self.count, 'note': note}
    return self.db[self.count]

  def delete_note(self, id):
    if id in self.db:
      del self.db[id]
    return

  def get_notes(self):
    return self.db.values()


database = Database()


# HTTPRequestHandler class
class todoHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  backend_path = "/todo"
  
  # GET
  def do_GET(self):
    self.send_response(200)
    if self.path == self.backend_path:
      self.send_header('Content-type','application/json')
      self.end_headers()
      notes = database.get_notes()
      self.wfile.write(json.dumps(notes))
    else:
      path = '../frontend/'
      if self.path=="/":
        self.path="index.html"
      elif self.path.endswith(".html"):
        mimetype='text/html'
        sendReply = True
      elif self.path.endswith(".js"):
        mimetype='application/javascript'
        sendReply = True
      elif self.path.endswith(".css"):
        mimetype='text/css'
        sendReply = True
      else:
        self.send_response(404)
        return
      f = open(curdir + sep + path + self.path)
      self.send_response(200)
      self.send_header('Content-type', mimetype)
      self.end_headers()
      self.wfile.write(f.read())
      f.close()
    return

  #POST
  def do_POST(self):
    if self.path == self.backend_path:
      length = int(self.headers['Content-length'])
      body = self.rfile.read(length)
      postvars = json.loads(body)
      note = postvars['todo']
      new_note = database.add_note(note)
      self.send_response(201)
      self.send_header('Content-type','application/json')
      self.end_headers()
      self.wfile.write(json.dumps(new_note))
    return

  def do_DELETE(self):
    if self.path.startswith(self.backend_path):
      id = int(self.path.split("/")[2])
      print(id)
      database.delete_note(id)
      self.send_response(200)
      self.end_headers()
    return

def run():
  print('starting server...')
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, todoHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


parser = argparse.ArgumentParser()
parser.add_argument("--run", help="Run the server",
                    action="store_true")
args = parser.parse_args()
if args.run:
  run()
