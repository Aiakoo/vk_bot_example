import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

API_KEY = ""
API_VER = ""

session = vk_api.VkApi(token=API_KEY, api_version=API_VER)
longpoll = VkLongPoll(session)
vk = session.get_api()
for event in longpoll.listen():
    while True:
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            print(
                f"Message: {event.message}\n"
                f"Attachments: {event.attachments}")