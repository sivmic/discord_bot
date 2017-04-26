import controllers.controller as controller


class Image(controller.Controller):
    async def process(self, params, message, client):
        await client.send_file(message.channel, '/home/ubuntu/handles_bot/handles.png')
