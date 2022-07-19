var ws = new WebSocket("ws://localhost:3000");

ws.onopen = function() {
    ws.send('hello wserver')
};

ws.onmessage = function (evt) { 
    message = evt.data
    alert(message)
};