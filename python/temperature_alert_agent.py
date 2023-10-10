# temperature_alert_agent.py

from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
from weather_api import fetch_temperature

class TemperatureRequest(Model):
    min_temperature: float
    max_temperature: float
    location: str

class TemperatureResponse(Model):
    message: str

# Creating the temperature agent 
temperature_alert_agent = Agent(
    name="temperature_alert_agent",
    port=8000,
    seed="temperature_alert_agent secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)

fund_agent_if_low(temperature_alert_agent.wallet.address())

# Function to send alert to the user if current temperature is out of bounds of provided min,max temperature
async def check_temperature_and_alert(ctx: Context,msg: TemperatureRequest,sender: str):
    # get the current temperature of the provided location
    current_temperature = fetch_temperature(msg.location)

    if current_temperature is not None:
        if current_temperature < msg.min_temperature:
            await ctx.send(sender, TemperatureResponse(message=f"Temperature Alert: It's too cold! Current temperature is {current_temperature}°C.")) 
        elif current_temperature > msg.max_temperature:
            await ctx.send(sender, TemperatureResponse(message=f"Temperature Alert: It's too hot! Current temperature is {current_temperature}°C.")) 

@temperature_alert_agent.on_message(model=TemperatureRequest, replies=TemperatureResponse)
async def handle_query_request(ctx: Context, sender: str, msg: TemperatureRequest):
    await check_temperature_and_alert(ctx,msg,sender)


if __name__ == "__main__":
    temperature_alert_agent.run()


# The below code can be used to get the address of this agent

# @temperature_alert_agent.on_event("startup")
# async def introduce_agent(ctx: Context):
#     ctx.logger.info(f"Hello, I'm agent {ctx.name} and my address is {ctx.address}.")