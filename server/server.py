#!/usr/bin/env python

import cgi
import json
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep

todo_list = []

# HTTPRequestHandler class
class todoHTTPServer_RequestHandler(BaseHTTPRequestHandler):


  def add_note(note):
    todo_list.append(note)
    return

  def remove_note(note):
    if note in todo_list:
      todo_list.remove(note)
    return

  # GET
  def do_GET(self):
    # Send response status code
    self.send_response(200)

    if self.path == "/todo":
      # Send headers
      self.send_header('Content-type','application/json')
      self.end_headers()

      # Write content as utf-8 data
      self.wfile.write(json.dumps(todo_list))
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
    if self.path == "/todo":
      length = int(self.headers['Content-length'])
      body = self.rfile.read(length)
      postvars = json.loads(body)
      note = postvars['todo']
      add_note(note)
      self.send_response(200, "OK")
      self.end_headers()
      self.wfile.write(json.dumps(todo_list))
    return

  def do_DELETE(self):
    if self.path == "/todo":
      length = int(self.headers['Content-length'])
      body = self.rfile.read(length)
      postvars = json.loads(body)
      note = postvars['todo']
      remove_note(note)
      self.send_response(200, "OK")
      self.end_headers()
      self.wfile.write(json.dumps(todo_list))
    return

def run():
  print('starting server...')
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, todoHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()