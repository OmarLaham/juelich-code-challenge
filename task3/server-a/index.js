//execute the code in "strict mode"
'use strict';

//require the express-ping to allow other servers to ping our server and check its internal status (https://www.npmjs.com/package/express-ping)
const health = require('express-ping');

//require the Express module and put it in the defined express constant
const express = require('express');

//import helper functions from utils.js
const utils = require('./utils');

// Constants
const PORT = process.env.PORT || 2000;
const HOST = '172.24.24.3';

// Functions
async function testDBConnectionWrap() {
	const test_db_res = await utils.testDBConnection();
	if (test_db_res === "Connection to postgres successful!") {
		const msg_success = '>>> Successfully connected to Postgres DB on DB Server.';
		//log to standart-out
		console.log(msg_success);
	} else {
		const msg_fail = '>>> Error. Unable to connect to Postgres DB on the DB Server.';
		//log to standart-out
		console.log(msg_fail);
	}
}

// App
const app = express();

// Define routes
// It's always better to define routes in a separate file, but for a simple application this is acceptable. 
// In all circumistances, I defined the routes in a separate file in Task 2

//home route
app.get('/', (req, res) => {
	res.send("Homepage");  
});

//add a new /ping endpoint to check the app status using 'express-ping'.
app.use(health.ping()); // this is the only addition

//list to PORT
app.listen(PORT);
console.log(`Server-A running on http://${HOST}:${PORT}`);

//check if can connect to db server
//wrap everything in an async function to be able to use 'await'
//set 3000ms timeout to wait till postgres server is up
setTimeout(testDBConnectionWrap, 3000);

