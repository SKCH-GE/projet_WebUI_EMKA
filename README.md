# PCB Cooking Oven Monitoring Solution

A monitoring system for PCB cooking ovens using the ESP32, which tracks sensor event changes and updates a local web application. The web app is hosted on a PC within a local network and provides real-time updates for monitoring the PCB cooking process.

## Features

- **ESP32-based sensor integration**: Monitors the PCB oven's sensors (temperature, humidity, etc.)
- **Local web app**: Hosted on a PC using Python Flask, providing a real-time interface for the user.
- **Real-time updates**: The webpage updates automatically based on sensor data changes.
- **Web interface**: Built with basic HTML, CSS, and JavaScript.
- **Easy setup**: `setup.py` script to manage dependencies and run the application.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/pcb-cooking-oven-monitoring.git
   cd pcb-cooking-oven-monitoring
   ```
2. Install dependencies:
   ```bash
   python setup.py install
   ```
3. Run the application:
   ```bash
   python app.py
   ```
   ***The app will be hosted on your local network and accessible via your browser at http://<PC_IP>:5000.***
## Setup

    Ensure that the ESP32 is connected and programmed to send sensor data over the network.
    Configure the ESP32 to communicate with the PC hosting the Flask server.
    Update any configuration settings (e.g., sensor details, network settings) in the config.py file.

## Technologies Used

    ESP32: For monitoring and sending sensor data.
    Python Flask: Web server for hosting the app.
    HTML/CSS/JavaScript: Frontend for the web app.
    setup.py: To manage dependencies and run the app.
