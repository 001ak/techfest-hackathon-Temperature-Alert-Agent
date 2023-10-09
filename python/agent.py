# agent.py

from uagents import Agent, Context, Bureau
from config import preferred_min_temperature, preferred_max_temperature, preferred_location
from weather_api import fetch_temperature

# Create the Temperature Alert Agent

# Define a starting port number
starting_port = 8001
user_agents = []
bureau = Bureau()
# Create the Temperature Alert Agent with an endpoint
temperature_alert_agent = Agent(
    name="temperature_alert_agent",
    seed="seed_phrase_here",
    endpoint=["http://127.0.0.1:8000/submit"],  # Replace with your desired endpoint
)
# adding dynamic users

# Function to add a new user agent dynamically
def add_user_agent():
    global starting_port  # Use a global variable to track the port number
    name = input("Enter user name: ")
    min_temperature = float(input("Enter minimum temperature: "))
    max_temperature = float(input("Enter maximum temperature: "))
    location = input("Enter preferred location: ")

    # Generate the endpoint URL based on the current port number
    endpoint = f"http://localhost:{starting_port}/submit"

    # Create a new user agent instance
    user_agent = Agent(name=name, seed=name, endpoint=[endpoint])

    # Increment the port number for the next user agent
    starting_port += 1

    # Add the new user agent instance to the bureau
    bureau.add(user_agent)

    # Create a new user agent configuration dictionary
    new_user_agent = {
        "name": name,
        "min_temperature": min_temperature,
        "max_temperature": max_temperature,
        "location": location,
        "endpoint": endpoint,
    }

    # Add the new user agent configuration dictionary to the list of user_agents
    user_agents.append(new_user_agent)

    # Log a message indicating the new user agent has been added
    print(f"User agent '{name}' added with temperature range ({min_temperature}°C - {max_temperature}°C) in {location} and endpoint {endpoint}.")


async def check_temperature_and_alert(ctx: Context):
    current_temperature = fetch_temperature(preferred_location)

    if current_temperature is not None:
        if current_temperature < preferred_min_temperature:
            ctx.logger.info(f"Temperature Alert: It's too cold! Current temperature is {current_temperature}°C.")
            
        elif current_temperature > preferred_max_temperature:
            ctx.logger.info(f"Temperature Alert: It's too hot! Current temperature is {current_temperature}°C.")
            

# Schedule the temperature check at regular intervals
@temperature_alert_agent.on_interval(period=10)  # Check every 10 seconds
async def temperature_check_interval(ctx: Context):
    await check_temperature_and_alert(ctx)

if __name__ == "__main__":
    temperature_alert_agent.run()
    # add_user_agent()
    # bureau.run()



