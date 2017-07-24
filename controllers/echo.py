import controllers.controller as controller


class Echo(controller.Controller):
    async def process(self, params, message, client):
        data = ' '.join(params)

        if params[0][0] == "!":
            data = "Just.. Dude stop"

        await client.delete_message(message)
        await client.send_message(message.channel, data)
