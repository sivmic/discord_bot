import controllers.controller as controller


class Image(controller.Controller):
    async def process(self, params, message, client):
        image_path = '/home/ubuntu/handles_bot/images/handles.png'
        if len(params) > 1:
            image_path = '/home/ubuntu/handles_bot/images/' + params[0]
        await client.send_file(message.channel, image_path)
