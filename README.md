# WebSocket Application

## Overview

This project demonstrates a WebSocket-based application that includes:

- A **Python WebSocket server** that handles client connections.
- A **Python client** for sending 10,000 automated messages to the server.
- An **HTML client** with a browser-based UI for manual interaction with the WebSocket server.

The server listens on `ws://localhost:8765` for connections from both clients. It processes the incoming messages by appending a random number and sends the modified message back to the client.

---

## Components

### 1. WebSocket Server (`websocket_server.py`)

The WebSocket server listens for connections and handles messages from clients by:
- Receiving a message.
- Appending a random number to the message.
- Sending the modified message back to the client.

### 2. Python WebSocket Client (`websocket_client.py`)

The Python WebSocket client:
- Connects to the WebSocket server.
- Sends 10,000 messages in an automated loop.
- Receives and prints the server’s responses to the terminal.

### 3. HTML WebSocket Client (`index.html`)

The HTML WebSocket client provides a browser interface where:
- Users can manually send messages to the server.
- The server's responses are displayed in real-time on the webpage.

---

## Prerequisites

- **Python 3.x** installed on your system.
- **`websockets`** library for Python:
  ```bash
  pip3 install websockets
  ```

---

## How to Run

### Step 1: Start the WebSocket Server

1. Open a terminal.
2. Navigate to the project directory.
3. Run the WebSocket server:
   ```bash
   python3 websocket_server.py
   ```

### Step 2: Run the Python WebSocket Client (Optional)

1. Open a new terminal window.
2. Navigate to the project directory.
3. Run the Python WebSocket client to send 10,000 messages:
   ```bash
   python3 websocket_client.py
   ```

The client will send messages in the format `Hello Server {i}`, where `i` is a counter from 0 to 9999, and print the server’s responses.

### Step 3: Open the HTML WebSocket Client

To manually interact with the WebSocket server via a browser:

1. Open a new terminal.
2. Navigate to the project directory.
3. Serve the `index.html` file using Python’s built-in HTTP server:
   ```bash
   python3 -m http.server 8000
   ```
4. Open a web browser and navigate to:
   ```
   http://localhost:8000
   ```

You can type messages into the input field and click **Send Message**. The server’s responses will be displayed in real-time on the page.

---

## Example Workflow

### Python WebSocket Client

- The Python client sends 10,000 messages automatically and prints responses.
- Example response: `Hello Server 0 87` (where `87` is a random number).

### HTML WebSocket Client

- You type a message in the browser input field (e.g., `"Hello Server"`) and the server responds with a modified message (e.g., `"Hello Server 45"`, where `45` is a random number).
- The response is displayed directly on the web page.

---

## Conclusion

This WebSocket application demonstrates both automated communication (using the Python client) and manual interaction (using the HTML client). It showcases real-time, two-way communication between clients and a server using the WebSocket protocol.

Feel free to extend or modify the project to suit more advanced use cases!

---
