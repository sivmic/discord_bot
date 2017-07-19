import controllers.controller as controller


class Echo(controller.Controller):
    async def process(self, params, message, client):
        data = ' '.join(params)
        # data += "\n\nSent from: " + message.author
        await client.delete_message(message)
        await client.send_message(message.channel, data)
