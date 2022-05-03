//require Postgres
const { Client } = require('pg');

// Create and export testDBConnection function to test connection with db
// Use async and await when dealing with external services and APIs for reliable connections.
async function testDBConnection() {
	
	//define postgres client instance using env variables exposed in Dockerfile
	const client = new Client({
		host: process.env.PG_HOST,
		port: process.env.PG_PORT,
		user: process.env.PG_USER,
		password: process.env.PG_PASSWORD,
		database: process.env.PG_DATABASE,
		ssl: false, //must use SSL in production
	});
	try {
	
		//connect to db
		await client.connect();
		//execute query
		const res = await client.query('SELECT $1::text as connected', ['Connection to postgres successful!']);
		//save query result to return later
		const message = res.rows[0].connected;
		//close connection
		await client.end();
		//return query result
		return message;
	
	} catch (err) {
		next(err);
	}
	
}

module.exports.testDBConnection = testDBConnection;
