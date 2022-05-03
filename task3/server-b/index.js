//execute the code in "strict mode"
'use strict';

//require the Express module and put it in the defined express constant
const express = require('express');

//import helper functions from utils.js
const utils = require('./utils');

// Constants
const PORT = process.env.SERVER_B_PORT || '3000';
const HOST = process.env.SERVER_B_HOST || '127.0.0.1';

// Functions

async function pingServerA() {

	//check the status of Server-A
	if (process.env.SERVER_A_HOST !== undefined && process.env.SERVER_A_PORT !== undefined) {

		//define some consts for better code readability
		const SERVER_A_HOST = process.env.SERVER_A_HOST;
		const SERVER_A_PORT = process.env.SERVER_A_PORT;
		console.log(`Checking connection with Server-A at ${SERVER_A_HOST}:${SERVER_A_PORT}`);
		
				
		await utils.checkConnection(SERVER_A_HOST, SERVER_A_PORT).then(function() {
		    //success
		    console.log('Server-A is alive');
		}, function(err) {
			//fail
		    console.log('Server-A is dead');
		})

	} else {
		const msg_fail = ">>> Must provide the HOST and PORT for Server-A";
	  	//log to standart-out
	  	console.log(msg_fail);
	}
	
}

// App
const app = express();

//define routes

//home route
app.get('/', (req, res) => {
	
	//render HTML for Hello, world page as response (extra points question)
	res.sendFile(__dirname + '/hello.html');
});

// All other routes will respond with access denied
app.get('/*', (req, res) => {
    res.send({ response: 'Task3-Server-B: Access Denied' });
});


//list to PORT on HOST
app.listen(PORT);
console.log(`Server-B running on http://${HOST}:${PORT}`);

//check Server-A status
//set 3000ms timeout to wait till Server-A is up
setTimeout(pingServerA, 3000);
