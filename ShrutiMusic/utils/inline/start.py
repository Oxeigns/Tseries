from pyrogram.types import InlineKeyboardButton
import config
from ShrutiMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=_["E_X_1"], url="https://t.me/TeamSirion"),
            InlineKeyboardButton(text="˹T Sᴇʀɪᴇs ᴍᴜsɪᴄʙᴏᴛ˼", url="https://t.me/tseries_musicbot"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["E_X_1"], url="https://t.me/Teamsirion"),
            InlineKeyboardButton(text="˹T Sᴇʀɪᴇs ᴍᴜsɪᴄʙᴏᴛ˼", url="https://t.me/tseries_musicbot")
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")
        ],
    ]
    return buttons
