let websocket = new WebSocket('ws://127.0.0.1:5010');

websocket.onmessage = (event) => {
  var msg = JSON.parse(event.data);

  if (msg.type === 'command' && msg.command === 'reload')
    window.location.reload();
};
