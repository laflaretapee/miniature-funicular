from aiogram import types


@dp.message_handler(commands=['start','help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')    
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Pizza_halal_bot')


@dp.message_handler(commands=['Режим работы'])
async def pizza_open_zavedenie(message : types.Message):
    await bot.send_message(message.from_user.id ,'Пн - Пт с 9:00 до 20:00, Сб-Вс с 10:00 до 22:00')


@dp.message_handler(commands=['Геолокация'])
async def geo_pizza(message : types.Message):
    await bot.send_message(message.from_user.id, 'ул. Медиков 51')
