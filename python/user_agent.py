# user.py

from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
import sys

# Address of temperature_alert agent
RECIPIENT_ADDRESS = "agent1qvlm6wpqggh9a8msqr77zkrl67djesfwm3ez9cl7q0jz3ckdw9nnz8erl4l"

# setting default values
prefered_min_temp=10.0
prefered_max_temp=30.0
prefered_location="New York"

class TemperatureRequest(Model):
    min_temperature: float
    max_temperature: float
    location: str

class TemperatureResponse(Model):
    message: str

# Taking port for user from command line
user_port=int(sys.argv[1])
SEED=f"seed_{user_port}"
ENDPOINT_URI=f"http://127.0.0.1:{user_port}/submit"

# Creating the user agent
user_agent = Agent(
    name="user_agent",
    port=user_port,
    seed=SEED,
    endpoint=[ENDPOINT_URI],
)

fund_agent_if_low(user_agent.wallet.address())

# on startup take input for min,max temperature and location from user
@user_agent.on_event("startup")
async def introduce_agent(ctx: Context):
    global prefered_min_temp,prefered_max_temp,prefered_location
    prefered_min_temp = float(input("Enter minimum temperature: "))
    prefered_max_temp = float(input("Enter maximum temperature: "))
    prefered_location = input("Enter preferred location: ")

# user communicates with the temperature_agent in an interval of 20 sec
# If temperature of provided location is out of bounds, user gets an Alert
@user_agent.on_interval(period=20.0, messages=TemperatureRequest)
async def interval(ctx: Context):
    completed = ctx.storage.get("completed")

    if not completed:
        await ctx.send(RECIPIENT_ADDRESS, TemperatureRequest(min_temperature=prefered_min_temp,max_temperature=prefered_max_temp,location=prefered_location))

@user_agent.on_message(model=TemperatureResponse, replies=TemperatureRequest)
async def handle_query_response(ctx: Context, sender: str, msg: TemperatureResponse):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")

if __name__ == "__main__":
    user_agent.run()
