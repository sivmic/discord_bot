import controllers.controller as controller


class Echo(controller.Controller):
    async def process(self, params, message, client):
        await client.send_message(message.channel, ' '.join(params))
