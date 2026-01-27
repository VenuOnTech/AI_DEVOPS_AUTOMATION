const express = require("express");
const app = express();

// Environment variables
const PORT = process.env.PORT || 3000;
const APP_VERSION = process.env.APP_VERSION || "local";

// Home route
app.get("/", (req, res) => {
  res.send(`
    <h1>🚀 AI DevOps Automation</h1>
    <p>Version: ${APP_VERSION}</p>
    <p>Status: Role B Ready</p>
  `);
});

// Health check
app.get("/health", (req, res) => {
  res.json({
    status: "UP",
    version: APP_VERSION,
    time: new Date().toISOString()
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
