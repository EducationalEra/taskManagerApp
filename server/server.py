#!/usr/bin/env python

import argparse
import cgi
import json
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
#from http.server import BaseHTTPRequestHandler, HTTPServer

class NoteList:

  def __init__(self):
        self.todo_list = []

  def add_note(self, note):
    self.todo_list.append(note)
    return

  def delete_note(self, note):
    if note in self.todo_list:
      self.todo_list.remove(note)
    return

  def get_notes(self):
    return self.todo_list


note_list = NoteList()

# HTTPRequestHandler class
class todoHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  backend_path = "/todo"

  # GET
  def do_GET(self):
    self.send_response(200)
    if self.path == backend_path:
      self.send_header('Content-type','application/json')
      self.end_headers()
      notes = note_list.get_notes()
      self.wfile.write(json.dumps(notes))
    else:
      path = '../frontend/'
      if self.path=="/":
        self.path="index.html"
      if self.path.endswith(".html"):
        mimetype='text/html'
        sendReply = True
      if self.path.endswith(".js"):
        mimetype='application/javascript'
        sendReply = True
      if self.path.endswith(".css"):
        mimetype='text/css'
        sendReply = True
      f = open(curdir + sep + path + self.path)
      self.send_response(200)
      self.send_header('Content-type', mimetype)
      self.end_headers()
      self.wfile.write(f.read())
      f.close()
    return

  #POST
  def do_POST(self):
    if self.path == backend_path:
      length = int(self.headers['Content-length'])
      body = self.rfile.read(length)
      postvars = json.loads(body)
      note = postvars['todo']
      note_list.add_note(note)
      self.send_response(200, "OK")
      self.end_headers()
      notes = note_list.get_notes()
      self.wfile.write(json.dumps(notes))
    return

  def do_DELETE(self):
    if self.path == backend_path:
      length = int(self.headers['Content-length'])
      body = self.rfile.read(length)
      postvars = json.loads(body)
      note = postvars['todo']
      note_list.delete_note(note)
      self.send_response(200, "OK")
      self.end_headers()
      notes = note_list.get_notes()
      self.wfile.write(json.dumps(notes))
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
