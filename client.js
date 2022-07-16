var ws = new WebSocket("wss://localhost:3000");

ws.onopen = function() {
    ws.send('connected')
};

ws.onmessage = function (evt) { 

};