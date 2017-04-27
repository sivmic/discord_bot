import controllers.controller as controller
import os


class Image(controller.Controller):
    async def process(self, params, message, client):
        image_path = '/home/ubuntu/handles_bot/images/handles.png'
        string = "Available images:\n\n"

        if len(params) > 0:
            if params[0] == 'help':
                data = next(os.walk("/home/ubuntu/handles_bot/images/"))[2]
                for i in range(len(data)):
                    string += "`" + data[i].replace('.png', ' ') + "`\n"
                await client.send_message(message.channel, string)

            image_path = '/home/ubuntu/handles_bot/images/' + params[0] + '.png'
        await client.send_file(message.channel, image_path)
