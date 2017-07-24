import controllers.controller as controller


class Echo(controller.Controller):
    async def process(self, params, message, client):
        tts = False
        if params[0][0] == ";":
            tts = True
            params[0] = params[0][1:]

        data = ' '.join(params)

        await client.delete_message(message)
        if params[0][0] == "!":
            image_path = '/home/ubuntu/handles_bot/images/dudestop.png'
            await client.send_file(message.channel, image_path)
        else:
            await client.send_message(message.channel, data, tts=tts)
