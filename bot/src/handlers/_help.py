from pyrogram import types, enums


async def _help_handler_callback(_, msg: types.Message) -> None:
    await msg.reply(
        'Бот проекта [SportHub](https://github.com/hackathonsrus/pp_50378_nr_21_kod_418_46) предназначен для получения'
        ' персонализированных уведомлений об интересующих вас событиях из единого'
        ' календаря спортивных мероприятий. Чтобы воспользоваться ботом, необходимо подключить учётную запись SportHub.',
        parse_mode=enums.ParseMode.MARKDOWN,
    )
