import controllers.controller as controller


class Image(controller.Controller):
    async def process(self, params, channel, client):
        await client.send_file(channel, '/home/ubuntu/handles_bot/handles.png')
