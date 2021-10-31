# functions.py
# A place to store all the "important" functions for the bot lol
# Author: wHo#6933

from io import StringIO


async def get_admins():
    # Returns a list of admin IDs, stored in STRINGs
    with open("admins.txt")as f:
        admins = f.readlines()
        f.close()

    return admins

async def check_admin(id: str):
    # Checks if an ID (STRING) is an admin
    admins = await get_admins()
    return (id in admins) # if id in admins, yes
                          # if id not in admins, no