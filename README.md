# techfest-hackathon-Temperature-Alert-Agent
Temperature Alert Agent using uAgent library

# Temperature Alert Agent

The Temperature Alert Agent is a dynamic project that leverages a free weather API to retrieve real-time temperature data for user-defined locations. It offers users the flexibility to establish their desired temperature thresholds and locations. Whenever the current temperature goes beyond these set parameters, the agent promptly sends out alerts. In conjunction with this, we've developed a Temperature Alert Agent capable of acquiring temperature information from the weather API. User agents are responsible for sending query requests to the Temperature Alert Agent, which in turn delivers responses to the user agents, making this a comprehensive and interactive system for real-time temperature monitoring and notifications.

Important: Multiple user agents can also query at a single timme.

## Setup

### 1. Clone the Project

Clone the project repository using the following command:

```bash
git clone https://github.com/001ak/techfest-hackathon-Temperature-Alert-Agent.git
```
### 2. Installation
2.1 Install Poetry
For Linux and macOS:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
For Windows (Run it in PowerShell):
```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
2.2 Install Dependencies
Navigate to the project's python directory and install dependencies using Poetry:
```bash
cd python
poetry install
poetry shell
```

2.3 Install the python-decouple library:
```bash
pip install python-decouple
```
### 3. Setting up Environment Variables
To set up the necessary environment variables:

Create a .env file in the root of the project directory if it doesn't already exist.

Obtain your Weather API key from  [Weather API Provider](https://www.weatherapi.com/)

Open the .env file and replace the placeholders with your API key:
```bash
WEATHER_API_KEY=your_api_key_here
```

### 4. Running the Project
First, run temperature_alert_agent.py in one terminal:
```bash
python temperature_alert_agent.py
```
It runs on port 8000.

Then, run user_agent.py in another terminal( Again perform **poetry shell** in this new terminal). It will prompt the user to provide inputs. Make sure to run it on a port other than 8000:
```bash
python user_agent.py port_no
```
If more users want to query, then run user_agent.py in more terminals with different port numbers.

Example:-
1st User Query
```bash
python user_agent.py 8001
```
2nd User Query
```bash
python user_agent.py 8002
```
The Temperature Alert Agent will fetch temperature data and send alerts based on the user's input.

## Description
Temperature agent is running on the 8000 port and for each user, a new agent will be created which will be running on the provided port so each user should be given a different port number where no process is running. Each time user agent will call the temperature agent after a specific amount of time for the temperature of a particular city. The seed for the user agent will be made using the port number so that each user has a different address and a response from the temprature agent will be sent back to specific user using the user's address.  
