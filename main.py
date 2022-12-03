from vkbottle import API
from vkbottle.user import User, Message
from config import token
import time

api = API(token)
user = User(token)


@user.on.message(text='test') # Декоратор ожидания входящих сообщений
async def handler(message: Message):
    members = await api.groups.get_members("public206090038") #Получаем участников сообщества
    members = members.items #Получаем id участников
    for people in members:
        time.sleep(15)
        await user.api.messages.send(people, message="hi", random_id=0)  # Отправляем сообщение

user.run_forever() #Запускаем UserBot-а
