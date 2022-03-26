from telethon import events

PM_IMG = "https://te.legra.ph/file/45ef597ef5ddc3039fc5c.jpg"
pm_caption = f"⚜ ROYALBot is Online ⚜ \n\n"
pm_caption += f"Owner ~ 『{royal_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Telethon ~ `1.15.0` \n"
pm_caption += f"┣『ROYALBot』~ `{ROYALversion}` \n"
pm_caption += f"┣Channel ~ [Channel](https://t.me/ROYALUSERBOT)\n"
pm_caption += f"┣**Licenece** ~ [Licence](https://github.com/ROYALBOY871/ROYALUSERBOT/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [ROYALBot』 ](https://t.me/ROYALBOY_XD)\n"
pm_caption += f"┣Assistant ~  [『ROYALBoy』 ](https://t.me/ROYALBOY_XD)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『LegendBot』](https://t.me/ROYALUSERBOT) «««"

from telethon import events


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
