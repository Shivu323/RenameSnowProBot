from pyrogram import Client, filters
from helper.database import db


# SETTING PREFIX & SUFFIX ✅
@Client.on_message(filters.private & filters.command('set_prefix'))
async def set_prefix(client, message):

    prefix = str(message.text).split()

    if len(prefix) == 1:
        await message.reply_text("""𝙶͏𝙸͏𝚅͏𝙴͏ 𝙼͏𝙴͏ 𝙰͏ 𝙿͏𝚁͏𝙴͏𝙵͏𝙸͏𝚇͏ 𝚃͏𝙾͏ 𝚂͏𝙴͏𝚃͏...!

𝙴͏𝚇͏𝙰͏𝙼͏𝙿͏𝙻͏𝙴͏ :

/set_prefix your_prefix""")
    

    else:
        prefix.remove('/set_prefix')
        final_prefix = ' '.join(prefix)
        SnowDev = await message.reply_text("𝙿𝚕𝚎𝚊𝚜𝚎 𝚆𝚊𝚒𝚝 ...")
        await db.set_prefix(message.from_user.id, final_prefix)
        await SnowDev.edit("𝚈𝚘𝚞𝚛 𝙿𝚛𝚎𝚏𝚒𝚡\n\n𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚂𝚊𝚟𝚎𝚍✅️")



@Client.on_message(filters.private & filters.command('set_suffix'))
async def set_suffix(client, message):

    prefix = str(message.text).split()
    user = message.from_user

    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)  

    elif len(prefix) == 1:
        await message.reply_text("""𝙶͏𝙸͏𝚅͏𝙴͏ 𝙼͏𝙴͏ 𝙰͏ 𝚂𝚄𝙵𝙵𝙸𝚇 𝚃͏𝙾͏ 𝚂͏𝙴͏𝚃͏...!

𝙴͏𝚇͏𝙰͏𝙼͏𝙿͏𝙻͏𝙴͏ :

/set_suffix your_suffix""")
    

    else:
        prefix.remove('/set_suffix')
        final_prefix = ' '.join(prefix)
        SnowDev = await message.reply_text("𝙿𝚕𝚎𝚊𝚜𝚎 𝚆𝚊𝚒𝚝 ...")
        await db.set_suffix(message.from_user.id, final_prefix)
        await SnowDev.edit("𝚈𝚘𝚞𝚛 𝚂𝚞𝚏𝚏𝚒𝚡\n\n𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚂𝚊𝚟𝚎𝚍✅️")



# RETRIEVING PREFIX & SUFFIX 🆘
@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_prefix(client, message):

    prefix = await db.get_prefix(message.from_user.id)
    if prefix:
        await message.reply_text(f"𝚈𝙾𝚄𝚁 𝙿𝚁𝙴𝙵𝙸𝚇 :\n\n {prefix}")

    elif prefix == "":
        await message.reply_text("""
𝚈𝙾𝚄 𝙳𝙾𝙽'𝚃 𝙷𝙰𝚅𝙴 𝙰𝙽𝚈 𝙿𝚁𝙴𝙵𝙸𝚇

𝚃𝙾 𝚂𝙴𝚃 𝚈𝙾𝚄𝚁 𝙲𝚄𝚂𝚃𝙾𝙼 𝙿𝚁𝙴𝙵𝙸𝚇

𝚄𝚂𝙴 <code> /set_prefix 𝙲𝙾𝙼𝙼𝙰𝙽𝙳...!""")



@Client.on_message(filters.private & filters.command('see_suffix'))
async def see_suffix(client, message):

    suffix = await db.get_suffix(message.from_user.id)
    if suffix:
        await message.reply_text(f"𝚈𝙾𝚄𝚁 𝚂𝚄𝙵𝙵𝙸𝚇 :\n\n {suffix}")

    elif suffix == "":
        await message.reply_text("""
𝚈𝙾𝚄 𝙳𝙾𝙽'𝚃 𝙷𝙰𝚅𝙴 𝙰𝙽𝚈 𝚂𝚄𝙵𝙵𝙸𝚇

𝚃𝙾 𝚂𝙴𝚃 𝚈𝙾𝚄𝚁 𝙲𝚄𝚂𝚃𝙾𝙼 𝚂𝚄𝙵𝙵𝙸𝚇

𝚄𝚂𝙴 /set_suffix 𝙲𝙾𝙼𝙼𝙰𝙽𝙳...!""")


# DELETING PREFIX & SUFFIX ❌
@Client.on_message(filters.private & filters.command('del_prefix'))
async def del_prefix(client, message):
    await db.set_prefix(message.from_user.id, prefix="")
    await message.reply_text("𝚈𝙾𝚄𝚁 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝙿𝚁𝙴𝙵𝙸𝚇\n\n𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈...! ❌️")



@Client.on_message(filters.private & filters.command('del_suffix'))
async def del_suffix(client, message):
    await db.set_suffix(message.from_user.id, suffix="")
    await message.reply_text("𝚈𝙾𝚄𝚁 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝚂𝚄𝙵𝙵𝙸𝚇\n\n𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈...! ❌️")
