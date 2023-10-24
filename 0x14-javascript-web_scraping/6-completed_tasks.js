#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from the first argument

if (!apiUrl) {
  console.error('Please provide the API URL as the first argument.');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code: ${response.statusCode}`);
  } else {
    try {
      const todos = JSON.parse(body);

      // Create a map to count completed tasks by user ID
      const completedTasksByUser = new Map();

      todos.forEach((todo) => {
        if (todo.completed) {
          const userId = todo.userId;
          completedTasksByUser.set(userId, (completedTasksByUser.get(userId) || 0) + 1);
        }
      });

      // Print users with completed tasks
      completedTasksByUser.forEach((count, userId) => {
        console.log(`User ID ${userId} has completed ${count} task(s).`);
      });
    } catch (parseError) {
      console.error('Error parsing JSON response:', parseError);
    }
  }
});
