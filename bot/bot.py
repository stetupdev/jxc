import discord
from discord import app_commands
from lexer import lexer
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Sync slash commands when bot is ready
@client.event
async def on_ready():
    await tree.sync()
    print(f"✅ Logged in as {client.user}")

# /genjxc command
@tree.command(name="genjxc", description="Generate JXC code from a prompt")
@app_commands.describe(prompt="Description for the JXC code to generate")
async def genjxc(interaction: discord.Interaction, prompt: str):
    # For now, placeholder generation
    generated_code = f'$ Generated JXC code for prompt: "{prompt}"\nuseJAVA\n#exampleVar 42\n{{\nPYTHONuse\n}}'
    await interaction.response.send_message(f"```jxc\n{generated_code}\n```")

# /jxclain command
@tree.command(name="jxclain", description="Explain a snippet of JXC code")
@app_commands.describe(code="The JXC code to explain")
async def jxclain(interaction: discord.Interaction, code: str):
    # Use lexer to tokenize
    tokens = lexer(code)
    explanation = "\n".join([f"- {kind}: {value}" for kind, value in tokens])
    await interaction.response.send_message(f"📝 Tokens:\n{explanation}")

# /jxcexplain command
@tree.command(name="jxcexplain", description="Explain the JXC language")
async def jxcexplain(interaction: discord.Interaction):
    explanation = (
        "JXC is a statically typed, garbage-collected, JIT-enabled language with custom syntax.\n"
        "Syntax highlights:\n"
        "- Blocks: `{ }`\n"
        "- Variables: `#varName`\n"
        "- Comments: `$ This is a comment`\n"
        "- Keywords: `useJAVA`, `PYTHONuse`, `UseCSHARP`, `Cplusplus`\n"
        "- Supports interoperability with Java, Python, C#, C++\n"
        "- File extension: `.jxc`"
    )
    await interaction.response.send_message(f"```jxc\n{explanation}\n```")

client.run(TOKEN)
