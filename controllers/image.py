import controllers.controller as controller


class Image(controller.Controller):
    async def process(self, params, message, client):
        image_path = '/home/ubuntu/handles_bot/images/handles.png'
        if len(params) > 0:
            image_path = '/home/ubuntu/handles_bot/images/' + params[0] + '.png'
        await client.send_file(message.channel, image_path)
