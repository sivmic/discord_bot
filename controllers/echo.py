import controllers.controller as controller


class Echo(controller.Controller):
    async def process(self, params, message, client):
        tts = False
        if params[0][0] == ";":
            tts = True
            params[0] = params[0][1:]

        data = ' '.join(params)

        if params[0][0] == "!":
            data = "Just.. Dude stop"

        await client.delete_message(message)
        await client.send_message(message.channel, data, tts=tts)
