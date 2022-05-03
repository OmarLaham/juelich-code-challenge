//require net and bluebird for pinging
const net = require('net');
const Promise = require('bluebird');

// Create and export checkConnection function to test connection with some host:port
// Default timeout = 10000ms
function checkConnection(host, port, timeout=10000) {
    return new Promise(function(resolve, reject) {
        
        var timer = setTimeout(function() {
            reject("timeout");
            socket.end();
        }, timeout);
        var socket = net.createConnection(port, host, function() {
            clearTimeout(timer);
            resolve();
            socket.end();
        });
        socket.on('error', function(err) {
            clearTimeout(timer);
            reject(err);
        });
    });
}

module.exports.checkConnection = checkConnection;
