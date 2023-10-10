# techfest-hackathon-Temperature-Alert-Agent
Temperature Alert Agent using uAgent library

# Temperature Alert Agent

Temperature Alert Agent is a project that connects to a free weather API to fetch real-time temperatures for specified locations. It allows users to set their preferred temperature range and location, and sends alerts when the current temperature exceeds the specified range.

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

Obtain your Weather API key from Weather API Provider.

Open the .env file and replace the placeholders with your API key:
WEATHER_API_KEY=your_api_key_here

### 4. Running the Project
First, run temp_agent.py in one terminal:
```bash
python temp_agent.py
```
It runs on port 8000.

Then, run user.py in another terminal. It will prompt the user to provide inputs. Make sure to run it on a port other than 8000:
```bash
python user.py
```
The Temperature Alert Agent will fetch temperature data and send alerts based on the user's input.
