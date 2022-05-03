const express = require('express');
const router = express.Router();

//define foo route
router.get('/foo', (req, res) => {
    res.json({ response: 'Hello' });
});

//define bar route
router.get('/bar', (req, res) => {
    res.json({ response: 'World' });
});

// All other routes will respond with access denied
router.get('/*', (req, res) => {
    res.json({ response: 'Task2: Access Denied' });
});

module.exports = router;

