import discord
from discord.ui import Select, View
from discord.ext import commands
import random
import os
import mmap
import fileinput
import time
current_dir = os.getcwd()

client = commands.Bot(command_prefix="u!", intents=discord.Intents.all())
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('u!help'))
    time.sleep(2)
    print("Restoring Blacklisted Users")
    time.sleep(2)    
    print("Restoring Open Ticket Button")
    time.sleep(2)
    print("Changing Status to u!help")
    time.sleep(2)
    print("TicketBot Is Online")


@client.command()
async def help(ctx):
  helpmembed = discord.Embed(title="UGEN | UGEN Commands", description="**User Commands**\n \n<:right:1063167391636398240> | u!help: Displays Help Menu. *Use: u!help*\n<:right:1063167391636398240> | u!gen: Allows you to gen accounts for free. *Use: u!gen*\n<:right:1063167391636398240> | u!stock: Displays all account stock. *Use: u!stock*\n \n**Dev/Mod Commands**\n \n<:right:1063167391636398240> | u!blacklist: Blacklists a User. *Use: u!blacklist (Userid/Username)*\n<:right:1063167391636398240> | u!rmblacklist: Removes a User from blacklist. *Use: u!rmblacklist (Userid/Username)*\n<:right:1063167391636398240> | u!whois: Shows a Users info. *Use: u!whois (Userid/Username)*", colour=0x009FE0)
  helpmembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
  helpmembed.set_footer(text="World's most advanced account generator.")
  await ctx.send(embed=helpmembed)

@client.command()
@commands.has_permissions(manage_roles=True)
async def blacklist(ctx, user:discord.Member):
  ui = user.id
  with open("bl.txt", "r+") as rf:
     data = rf.read()
     if str(ui) in data:
       await ctx.send(f"User {user.mention} is already in blacklist.")
     if str(ui) not in data:
       with open("bl.txt", "a") as file:
         file.write(f"{ui}\n")
         await ctx.send(f"{user.mention} have been added to blacklist")

    


@client.command()
@commands.has_permissions(manage_roles=True)
async def rmblacklist(ctx, user: discord.Member):
  ru = user.id
  with open("bl.txt", "r+") as rf:
    rd = rf.read()
    if str(user.id) in rd:
      newcon = rd.replace(f"{user.id}", f" ")
      with open("bl.txt", "w") as nf:
        nf.write(newcon)
        await ctx.send(f"User {user.mention} have been deleted from blacklist.")
    elif str(user.id) not in rd:
      await ctx.reply(f"User {user.mention} is not in the black list.")

      

@client.command()
@commands.has_permissions(manage_roles=True)
async def whois(ctx, user: discord.Member = None):
  if user==None:
    user=ctx.author
  rlist = []
  for role in user.roles:
    if role.name != "@everyone":
      rlist.append(role.mention)
  b = ','.join(rlist)
  infoembed = discord.Embed(title=f"User Info - {user}", colour=0x009FE0)
  infoembed.set_footer(text=f"World's most advanced account generator. Requested by - {ctx.author}", icon_url=user.display_avatar)
  infoembed.add_field(name="ID:", value=f"{user.id}", inline=False)
  infoembed.add_field(name="Name:", value=f"{user.display_name}", inline=False)
  infoembed.set_thumbnail(url=user.display_avatar)
  infoembed.add_field(name="Created at:", value=user.created_at, inline=False)
  infoembed.add_field(name="Joined at:", value=user.joined_at, inline=False)
  infoembed.add_field(name=f"Roles: ({len(rlist)})", value=''.join([b]), inline=False)
  infoembed.add_field(name="Top role:", value=user.top_role.mention, inline=False)
  infoembed.add_field(name="Is bot?", value=user.bot, inline=False)  
  await ctx.send(embed=infoembed)





@client.command(pass_context=True)
async def gen(ctx, member: discord.Member = None):
  channel = discord.utils.get(client.get_all_channels(), id=1058864993090666626)

  channelp = discord.utils.get(client.get_all_channels(), id=1059553917127630868)

  if ctx.channel.id == channel.id or ctx.channel.id == channelp.id:
    # Right Channel
    if member == None:
     member = ctx.author

     with open("bl.txt", "r+") as rf:
       dt = rf.read()
     if str(ctx.author.id) in dt:
       blembed = discord.Embed(title="Blacklist", description=f"Error {ctx.author.mention} you are on the blacklist.", colour=0x009FE0)
       blembed.set_footer(text="World's most advanced account generator.")
       await ctx.send(embed=blembed)
     else:
       # Have Premium

        role = discord.utils.find(lambda r: r.id == 1059554298972868671, ctx.message.guild.roles)
      
        if role in ctx.author.roles:
            embed42 = discord.Embed(title="UGEN", description=f"Which UGEN tier would you like to select from today, {ctx.author.mention}?", colour=0x009FE0)
            embed42.set_image(url="https://cdn.discordapp.com/attachments/1059562752768745623/1063154900390903828/standard_31.gif")
            embed42.set_footer(text="World's most advanced account generator.")
            view = Prime(ctx.author)
            view.timeout = 8
            await ctx.send(embed=embed42, view=view)    

      # Dont have Premium
       
        elif role not in ctx.author.roles:
            embed42 = discord.Embed(title="UGEN", description=f"Which UGEN tier would you like to select from today, {ctx.author.mention}?", colour=0x009FE0)
            embed42.set_image(url="https://cdn.discordapp.com/attachments/1059562752768745623/1063154900390903828/standard_31.gif")
            embed42.set_footer(text="World's most advanced account generator.")
            view = Free(ctx.author)
            view.timeout = 8
            await ctx.send(embed=embed42, view=view)
    else:
      return


      # Wrong channel
  elif ctx.channel.id is not channel.id:
    errorembed = discord.Embed(title="Wrong Channel", colour=0x009FE0)
    await ctx.send(embed=errorembed)
    
        





  

  
       

      

class FreeStock():
       with open(f"{current_dir}/data/Crunchyroll.txt", 'r') as cstock:
        for ccount, line in enumerate(cstock):
            pass
       with open(f"{current_dir}/data/Filmora.txt", 'r') as fstock:
        for fcount, line in enumerate(fstock):
            pass
       with open(f"{current_dir}/data/Nordvpn.txt", 'r') as nstock:
        for ncount, line in enumerate(nstock):
            pass
       with open(f"{current_dir}/data/Steam.txt", 'r') as sstock:
        for scount, line in enumerate(sstock):
            pass
       with open(f"{current_dir}/data/Duolingo.txt", 'r') as dustock:
        for ducount, line in enumerate(dustock):
            pass



class PremiumStock():
       with open(f"{current_dir}/blacklistusers/Valorant.txt", 'r') as vstock:
        for vcount, line in enumerate(vstock):
            pass
       with open(f"{current_dir}/blacklistusers/Mailaccess.txt", 'r') as mstock:
        for mcount, line in enumerate(mstock):
            pass
       with open(f"{current_dir}/blacklistusers/Disney.txt", 'r') as dstock:
        for dcount, line in enumerate(dstock):
            pass
        
@client.command()
async def stock(ctx):
  freeembed = discord.Embed(title="UGEN Freebie",
  description=
  f"<:crunchyroll:1063159356927000587> | Crunchyroll: **{FreeStock.ccount + 1}**\n<:filmora:1063159477169291394> | Filmora: **{FreeStock.fcount + 1}**\n<:nordvpn:1063159623089127444> | NordVpn: **{FreeStock.ncount + 1}**\n<:steam:1063159770992869447> | Steam: **{FreeStock.scount + 1}**\n<:duolingo:1063506587727183932> | Duolingo: **{FreeStock.ducount + 1}**", colour=0x009FE0)
  freeembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
  freeembed.set_image(url='https://cdn.discordapp.com/attachments/971263589019177022/996573362308513792/image0-19.jpg')
  freeembed.set_footer(text="World's most advanced account generator.")

  premiumembed = discord.Embed(title="UGEN Premium", description=
  f"<:valorant:1063159887409987684> | Valorant: **{PremiumStock.vcount + 1}**\n<:MailAccess:1063160073737736303> | MailAccess: **{PremiumStock.mcount + 1}**\n<:disney:1063853373792727120> | Disney Plus: **{PremiumStock.dcount + 1}**", colour=0x009FE0)
  premiumembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
  premiumembed.set_image(url='https://cdn.discordapp.com/attachments/1059562752768745623/1063154900390903828/standard_31.gif')
  premiumembed.set_footer(text="World's most advanced account generator.")

  await ctx.send(embed=freeembed)
  await ctx.send(embed=premiumembed)


class Prime(discord.ui.View):
 
    def __init__(self, author):
        self.author = author
        super().__init__()
  
    @discord.ui.button(label="Freebie", style=discord.ButtonStyle.success, emoji='<:Leacher:1053485092640657518>')
    async def freebie(self, interaction: discord.Interaction, button: discord.ui.Button):   

   

      embed2 = discord.Embed(title="UGEN",  description="Feel free to select account you want to generate!", colour=0x009FE0)
      embed2.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
      embed2.set_footer(text="World's most advanced account generator.")

   
      select = FreeGen()
      view = View(timeout=8)
      view.add_item(select)
      await interaction.response.send_message(view=view, embed=embed2, ephemeral=True)

    async def interaction_check(self, interaction: discord.Interaction):
      return interaction.user.id == self.author.id

      
      
   




      # Button 2

    @discord.ui.button(label="Premium", style=discord.ButtonStyle.danger, emoji='<:Premium:1053485090828714086>')
    async def normal(self, interaction: discord.Interaction, button: discord.ui.Button):   

      embedp = discord.Embed(title="UGEN Premium",  description="Feel free to select account you want to generate!", colour=0x009FE0)
      embedp.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
      embedp.set_footer(text="World's most advanced account generator.")


      select = PremiumGen()
      view = View(timeout=8)
      view.add_item(select)
      await interaction.response.send_message(view=view, embed=embedp, ephemeral=True)
    async def interaction_check(self, interaction: discord.Interaction):
      return interaction.user.id == self.author.id

   


class Free(discord.ui.View):
 
   
    def __init__(self, author):
        self.author = author
        super().__init__()

    @discord.ui.button(label="Freebie", style=discord.ButtonStyle.success, emoji='<:Leacher:1053485092640657518>')
    async def freebie(self, interaction: discord.Interaction, button: discord.ui.Button):   

   

      embed2 = discord.Embed(title="UGEN",  description="Feel free to select account you want to generate!", colour=0x009FE0)
      embed2.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
      embed2.set_footer(text="World's most advanced account generator.")


      select = FreeGen()
      view = View(timeout=8)
      view.add_item(select)
      await interaction.response.send_message(view=view, embed=embed2, ephemeral=True)
    async def interaction_check(self, interaction: discord.Interaction):
      return interaction.user.id == self.author.id




      # Button 2

    @discord.ui.button(label="Premium", style=discord.ButtonStyle.danger, emoji='<:Premium:1053485090828714086>', disabled=True)
    async def normal(self, interaction: discord.Interaction, button: discord.ui.Button):   

      embedp = discord.Embed(title="UGEN Premium",  description="Feel free to select account you want to generate!", colour=0x009FE0)
      embedp.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
      embedp.set_footer(text="World's most advanced account generator.")


      select = PremiumGen()
      view = View(timeout=8)
      view.add_item(select)
      await interaction.response.send_message(view=view, embed=embedp, ephemeral=True)
    async def interaction_check(self, interaction: discord.Interaction):
      return interaction.user.id == self.author.id

   

      
class PremiumGen(Select):
      # Dropdown Menu
    

       def __init__(self, ) -> None:   
        super().__init__(placeholder="Choose your premium account", 
        options=[

         discord.SelectOption(label=f"Valorant", emoji="<:Valorant:1049132081600548895>", value="Valorant"),
         discord.SelectOption(label=f"MailAccess", emoji="<:Mail_iOS:1062739466759966770>", value="Mailaccess"),
         discord.SelectOption(label=f"Disney", emoji="<:disney:1063853373792727120>", value="Disney"),
        


        
         ])



       async def callback(self, interaction):

     
       
        if self.values[0] == "Valorant":

         with open(f'{current_dir}/blacklistusers/{self.values[0]}.txt','r+') as accounts:
            data = accounts.readlines()
            randomaccount = random.choice(data)
            dmembed = discord.Embed(title=f"{self.values[0]} Account", description=f"Your {self.values[0]} account has been generated below:\n```{randomaccount}```\n*Thank you for using UGEN!*", colour=0x009FE0)
            dmembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
            dmembed.set_footer(text="World's most advanced account generator.")
           
            # Channel Embed
            chembed = discord.Embed(title="Account Generated!", description=f"Hello, {interaction.user.mention}!\n\n*UGEN has sent the account in a private message, check your DMs!*", colour=0x009FE0)   
            chembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
            chembed.set_footer(text="World's most advanced account generator.")

            logembed = discord.Embed(title=f"Account Generated By {interaction.user}",colour=0x009FE0)
            logembed.add_field(name="**Service:**", value=f"**{self.values[0]}**", inline=False)
            logembed.add_field(name="**Account:**", value=f"```{randomaccount}```", inline=False)
            logembed.set_footer(text="World's most advanced account generator.")
            channel = client.get_channel(1059187643776249956) # Log Channel

            await channel.send(embed=logembed)
            await interaction.user.send(embed=dmembed)
            await interaction.response.send_message(embed=chembed, ephemeral=True)
            
        elif self.values[0] == "Mailaccess":
           with open(f'{current_dir}/blacklistusers/{self.values[0]}.txt','r+') as accounts:
            data = accounts.readlines()
            randomaccount = random.choice(data)
            dmembed = discord.Embed(title=f"{self.values[0]} Account", description=f"Your {self.values[0]} account has been generated below:\n```{randomaccount}```\n*Thank you for using UGEN!*", colour=0x009FE0)
            dmembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
            dmembed.set_footer(text="World's most advanced account generator.")
           
            # Channel Embed
            chembed = discord.Embed(title="Account Generated!", description=f"Hello, {interaction.user.mention}!\n\n*UGEN has sent the account in a private message, check your DMs!*", colour=0x009FE0)   
            chembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
            chembed.set_footer(text="World's most advanced account generator.")

            logembed = discord.Embed(title=f"Account Generated By {interaction.user}",colour=0x009FE0)
            logembed.add_field(name="**Service:**", value=f"**{self.values[0]}**", inline=False)
            logembed.add_field(name="**Account:**", value=f"```{randomaccount}```", inline=False)
            logembed.set_footer(text="World's most advanced account generator.")
            channel = client.get_channel(1059187643776249956) # Log Channel

            await channel.send(embed=logembed)
            await interaction.user.send(embed=dmembed)
            await interaction.response.send_message(embed=chembed, ephemeral=True)


        elif self.values[0] == "Disney":
           with open(f'{current_dir}/blacklistusers/{self.values[0]}.txt','r+') as accounts:
            data = accounts.readlines()
            randomaccount = random.choice(data)
            dmembed = discord.Embed(title=f"{self.values[0]} Account", description=f"Your {self.values[0]} account has been generated below:\n```{randomaccount}```\n*Thank you for using UGEN!*", colour=0x009FE0)
            dmembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
            dmembed.set_footer(text="World's most advanced account generator.")
           
            # Channel Embed
            chembed = discord.Embed(title="Account Generated!", description=f"Hello, {interaction.user.mention}!\n\n*UGEN has sent the account in a private message, check your DMs!*", colour=0x009FE0)   
            chembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
            chembed.set_footer(text="World's most advanced account generator.")

            logembed = discord.Embed(title=f"Account Generated By {interaction.user}",colour=0x009FE0)
            logembed.add_field(name="**Service:**", value=f"**{self.values[0]}**", inline=False)
            logembed.add_field(name="**Account:**", value=f"```{randomaccount}```", inline=False)
            logembed.set_footer(text="World's most advanced account generator.")
            channel = client.get_channel(1059187643776249956) # Log Channel

            await channel.send(embed=logembed)
            await interaction.user.send(embed=dmembed)
            await interaction.response.send_message(embed=chembed, ephemeral=True)
   
        
          
            

    
    






class FreeGen(Select):
      # Dropdown Menu
    

       def __init__(self, ) -> None:   
        super().__init__(placeholder="Choose your free account", 
        options=[

         discord.SelectOption(label=f"Crunchyroll", emoji="<:Crunchyroll:1048875894120386570>", value="Crunchyroll"),
         discord.SelectOption(label=f"Filmora", emoji="<:Filmora:1049131112586301471>", value="Filmora"),
         discord.SelectOption(label=f"NordVpn", emoji="<:NordVPN:1048875988588703795>", value="Nordvpn"),
         discord.SelectOption(label=f"Steam", emoji="<:Steam:1049131231821955112>", value="Steam"),
         discord.SelectOption(label=f"Duolingo", emoji="<:duolingo:1063506587727183932>", value="Duolingo"),


        
         ])



       async def callback(self, interaction):

     
       
        if self.values[0] == "Crunchyroll":
         with open(f'{current_dir}/data/{self.values[0]}.txt','r+') as accounts:
            data = accounts.readlines()
            randomaccount = random.choice(data)
            dmembed = discord.Embed(title=f"{self.values[0]} Account", description=f"Your {self.values[0]} account has been generated below:\n```{randomaccount}```\n*Thank you for using UGEN!*", colour=0x009FE0)
            dmembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
            dmembed.set_footer(text="World's most advanced account generator.")
           
            # Channel Embed
            chembed = discord.Embed(title="Account Generated!", description=f"Hello, {interaction.user.mention}!\n\n*UGEN has sent the account in a private message, check your DMs!*", colour=0x009FE0)   
            chembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
            chembed.set_footer(text="World's most advanced account generator.")

            logembed = discord.Embed(title=f"Account Generated By {interaction.user}",colour=0x009FE0)
            logembed.add_field(name="**Service:**", value=f"**{self.values[0]}**", inline=False)
            logembed.add_field(name="**Account:**", value=f"```{randomaccount}```", inline=False)
            logembed.set_footer(text="World's most advanced account generator.")
            channel = client.get_channel(1059187643776249956) # Log Channel


            await channel.send(embed=logembed)
            await interaction.user.send(embed=dmembed)
            await interaction.response.send_message(embed=chembed, ephemeral=True)
            
        elif self.values[0] == "Filmora":
           with open(f'{current_dir}/data/{self.values[0]}.txt','r+') as accounts:
            data = accounts.readlines()
            randomaccount = random.choice(data)
            dmembed = discord.Embed(title=f"{self.values[0]} Account", description=f"Your {self.values[0]} account has been generated below:\n```{randomaccount}```\n*Thank you for using UGEN!*", colour=0x009FE0)
            dmembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
            dmembed.set_footer(text="World's most advanced account generator.")
           
            # Channel Embed
            chembed = discord.Embed(title="Account Generated!", description=f"Hello, {interaction.user.mention}!\n\n*UGEN has sent the account in a private message, check your DMs!*", colour=0x009FE0)   
            chembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
            chembed.set_footer(text="World's most advanced account generator.")


            logembed = discord.Embed(title=f"Account Generated By {interaction.user}",colour=0x009FE0)
            logembed.add_field(name="**Service:**", value=f"**{self.values[0]}**", inline=False)
            logembed.add_field(name="**Account:**", value=f"```{randomaccount}```", inline=False)
            logembed.set_footer(text="World's most advanced account generator.")
            channel = client.get_channel(1059187643776249956) # Log Channel


            await channel.send(embed=logembed)
            await interaction.user.send(embed=dmembed)
            await interaction.response.send_message(embed=chembed, ephemeral=True)
            
        elif self.values[0] == "Nordvpn":
           with open(f'{current_dir}/data/{self.values[0]}.txt','r+') as accounts:
            data = accounts.readlines()
            randomaccount = random.choice(data)
            dmembed = discord.Embed(title=f"{self.values[0]} Account", description=f"Your {self.values[0]} account has been generated below:\n```{randomaccount}```\n*Thank you for using UGEN!*", colour=0x009FE0)
            dmembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
            dmembed.set_footer(text="World's most advanced account generator.")
           
            # Channel Embed
            chembed = discord.Embed(title="Account Generated!", description=f"Hello, {interaction.user.mention}!\n\n*UGEN has sent the account in a private message, check your DMs!*", colour=0x009FE0)   
            chembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
            chembed.set_footer(text="World's most advanced account generator.")


            logembed = discord.Embed(title=f"Account Generated By {interaction.user}",colour=0x009FE0)
            logembed.add_field(name="**Service:**", value=f"**{self.values[0]}**", inline=False)
            logembed.add_field(name="**Account:**", value=f"```{randomaccount}```", inline=False)
            logembed.set_footer(text="World's most advanced account generator.")
            channel = client.get_channel(1059187643776249956) # Log Channel


            await channel.send(embed=logembed)
            await interaction.user.send(embed=dmembed)
            await interaction.response.send_message(embed=chembed, ephemeral=True)
      

 
        elif self.values[0] == "Steam":
       
          with open(f'{current_dir}/data/{self.values[0]}.txt','r+') as accounts:
            data = accounts.readlines()
            randomaccount = random.choice(data)
            dmembed = discord.Embed(title=f"{self.values[0]} Account", description=f"Your {self.values[0]} account has been generated below:\n```{randomaccount}```\n*Thank you for using UGEN!*", colour=0x009FE0)
            dmembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
            dmembed.set_footer(text="World's most advanced account generator.")
           
            # Channel Embed
            chembed = discord.Embed(title="Account Generated!", description=f"Hello, {interaction.user.mention}!\n\n*UGEN has sent the account in a private message, check your DMs!*", colour=0x009FE0)   
            chembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
            chembed.set_footer(text="World's most advanced account generator.")
            

            logembed = discord.Embed(title=f"Account Generated By {interaction.user}",colour=0x009FE0)
            logembed.add_field(name="**Service:**", value=f"**{self.values[0]}**", inline=False)
            logembed.add_field(name="**Account:**", value=f"```{randomaccount}```", inline=False)
            logembed.set_footer(text="World's most advanced account generator.")
            channel = client.get_channel(1059187643776249956) # Log Channel

            await channel.send(embed=logembed)
            await interaction.user.send(embed=dmembed)
            await interaction.response.send_message(embed=chembed, ephemeral=True)

        elif self.values[0] == "Duolingo":
       
          with open(f'{current_dir}/data/{self.values[0]}.txt','r+') as accounts:
            data = accounts.readlines()
            randomaccount = random.choice(data)
            dmembed = discord.Embed(title=f"{self.values[0]} Account", description=f"Your {self.values[0]} account has been generated below:\n```{randomaccount}```\n*Thank you for using UGEN!*", colour=0x009FE0)
            dmembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
            dmembed.set_footer(text="World's most advanced account generator.")
           
            # Channel Embed
            chembed = discord.Embed(title="Account Generated!", description=f"Hello, {interaction.user.mention}!\n\n*UGEN has sent the account in a private message, check your DMs!*", colour=0x009FE0)   
            chembed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1059186168106860594/2167c84749b3eed28c84d8f73ddd3b1a.png?size=256")
            chembed.set_footer(text="World's most advanced account generator.")
            

            logembed = discord.Embed(title=f"Account Generated By {interaction.user}",colour=0x009FE0)
            logembed.add_field(name="**Service:**", value=f"**{self.values[0]}**", inline=False)
            logembed.add_field(name="**Account:**", value=f"```{randomaccount}```", inline=False)
            logembed.set_footer(text="World's most advanced account generator.")
            channel = client.get_channel(1059187643776249956) # Log Channel

            await channel.send(embed=logembed)
            await interaction.user.send(embed=dmembed)
            await interaction.response.send_message(embed=chembed, ephemeral=True)
        
          
            
        
    
           # End of dropdown menu









client.run("MTA1OTE4NjE2ODEwNjg2MDU5NA.Gn2TCf.-IJRB6NeVq8SFaYRJjAxJy22zbqMM71RtnBSkk")


