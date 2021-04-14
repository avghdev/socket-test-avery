$(document).ready(function () {
    console.log("http://" + document.domain + ":" + location.port + "/test");
    var socket = io.connect("http://" + document.domain + ":" + location.port + "/test");

    socket.on("my connection", function (msg) {
        $("#log").append("<p style=\"color: green\">Status: " + msg.data + "</p>");
    });

    socket.on("new message", function (msg) {
        $("#log").append("<p>Recieved: " + msg.data + "</p>");
    });

    $("form#message").submit(function (event) {
        console.log("hi");
        socket.emit("my new message", { data: $("#message_data").val() });
        document.getElementById("message").reset();

        return false;
    });

});