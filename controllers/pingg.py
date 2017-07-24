import controllers.controller as controller
import datetime


class Pingg(controller.Controller):
    async def process(self, params, message, client):
        ping = datetime.datetime.utcnow() - message.timestamp
        time = ping.total_seconds()

        data = "Pongg!\n" + str(time) + "s"

        await client.delete_message(message)
        await client.send_message(message.channel, data)
