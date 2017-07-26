import controllers.controller as controller
import os


class Image(controller.Controller):
    async def process(self, params, message, client):
        string = "Available images:\n\n"

        if len(params) > 0:
            if params[0] == 'help':
                images = next(os.walk("/home/ubuntu/handles_bot/images/"))[2]
                for image in images:
                    string += "`" + image.replace('.png', ' ') + "`\n"
                await client.send_message(message.channel, string)
            else:
                image_path = '/home/ubuntu/handles_bot/images/' + params[0] + '.png'
                data = "Sent by: **" + str(message.author.nick) + "**"
                data_for_sickfucks = "For this fucking idiot: **" + str(
                    message.author.nick) + "**\n**" + ' '.join(params) + "** is **NOT** supported!"

                await client.delete_message(message)

                if os.path.isfile(image_path):
                    await client.send_message(message.channel, data)
                    await client.send_file(message.channel, image_path)
                else:
                    await client.send_message(message.channel, data_for_sickfucks)
