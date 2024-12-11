from discord import app_commands, Intents, Client

TOKEN ="TOKEN"

intents = Intents.default()
client = Client(intents=intents)
@client.event
async def on_ready():
    print("c nul le qwerty")
    await tree.sync()

intents.message_content = True
tree = app_commands.CommandTree(client)

@client.event
async def on_message(message):
	if message.content == 'ping':
		await message.channel.send('pong')
@tree.command(name = "plus", description = "simple addition")
async def addition_cmd(ctx,a:int,b:int):
    await ctx.response.send_message(f"The calculation resultis:\n{a+b}" )

client.run(TOKEN)

