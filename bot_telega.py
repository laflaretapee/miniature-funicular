from aiogram.utils import executor
from create_bot import dp


import os 



async def on_startup(_):
    print('Online')


from handlers import client,admin,other

client.register_handlers_client(dp)






executor.start_polling(dp, skip_updates= True,on_startup=on_startup)