const express = require('express');
const loggerMiddleware = require('./loggerMiddleware'); // Import middleware

const app = express();
const PORT = process.env.PORT || 3000;

// Use the logger middleware
app.use(loggerMiddleware);

// Example route
app.get('/', (req, res) => {
    res.send('Hello, World!');
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
