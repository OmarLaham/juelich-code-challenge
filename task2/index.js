//execute the code in "strict mode"
'use strict';

//require the Express module and put it in the defined express constant
const express = require('express');


// Constants. Use exposed env vars from Dockerfile if available. Otherwise, use default values
const PORT = process.env.PORT || 5000;
const HOST = '127.0.0.1';
const BASE_URL= process.env.BASE_URL || "/conabio";

// App
const app = express();

// Make Express pass '2' as the 3rd argument to `JSON.stringify()`
app.set('json spaces', 2);

//require routes from separate routes.js file
const router = require('./routes'); 
app.use(BASE_URL, router);

//list to PORT on HOST
app.listen(PORT);
console.log(`Running on http://${HOST}:${PORT}${BASE_URL}`);
