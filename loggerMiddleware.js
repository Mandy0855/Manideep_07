// loggerMiddleware.js

const loggerMiddleware = (req, res, next) => {
    console.log(`[${new Date().toISOString()}] ${req.method} request to ${req.url}`);
    next();
};

module.exports = loggerMiddleware;
