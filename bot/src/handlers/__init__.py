from pyrogram import filters
from pyrogram.handlers import MessageHandler

from ._start import _start_handler_callback
from ._help import _help_handler_callback


start = MessageHandler(
    _start_handler_callback,
    filters.private & filters.command('start'),
)
help_ = MessageHandler(
    _help_handler_callback,
    filters.private & filters.command('help'),
)
