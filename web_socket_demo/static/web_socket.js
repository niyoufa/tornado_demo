
$(function(){
    setTimeout(requestInventory, 100);
});

function requestInventory() {
    var host = 'ws://localhost:8000/send';

    var websocket = new WebSocket(host);

    websocket.onopen = function (evt) {websocket.send("hello") ; };
    websocket.onmessage = function(evt) {
        document.write(evt.data);
    };
    websocket.onerror = function (evt) {};
}