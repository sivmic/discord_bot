import controllers.controller as controller
import os


class Helpp(controller.Controller):
    async def process(self, params, message, client):
        data = next(os.walk("/home/ubuntu/handles_bot/controllers/"))[2]
        data.remove("controller.py")
        string = "Available commands:\n\n"

        for i in range(len(data)):
            string += "`!" + data[i].replace('.py', ' ') + "`\n"

        await client.delete_message(message)
        await client.send_message(message.channel, string)
