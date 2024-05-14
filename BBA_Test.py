import requests
import concurrent.futures
import re

import websocket,json

ws = websocket.WebSocket()
ws.connect("ws://www.heroku.com")
d = {"message": "hello"}
data = str(json.dumps(d))
ws.send(data)
result = ws.recv()
print(json.loads(result))
# d = {"message": "<script>alert(1)</script>"}
################################
import WebSocket from 'ws';

const accessToken = 'your_access_token_here';
const ws = new WebSocket(`wss://api.github.com/?access_token=${accessToken}`);

ws.on('error', console.error);

ws.on('open', function open() {
  console.log('Connected to GitHub WebSocket API with authentication');
});

ws.on('message', function message(data) {
  console.log('Received message from GitHub WebSocket API:', data);
});

ws.on('close', function close() {
  console.log('Disconnected from GitHub WebSocket API with authentication');
});