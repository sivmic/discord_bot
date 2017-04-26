import controllers.controller as controller


class Echo(controller.Controller):
    async def process(self, params, channel, client):
        await client.send_message(channel, ' '.join(params))
