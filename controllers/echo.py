import controllers.controller as controller


class Echo(controller.Controller):
    async def process(self, params, message, client):
        data = ' '.join(params)
        #data += "\n\nRepeated from: " + message.author.nick
        await client.send_message(message.channel, data)
