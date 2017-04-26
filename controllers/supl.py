import controllers.controller as controller


class Supl(controller.Controller):
    async def process(self, params, message, client):
        await client.send_message(message.channel, "Gideon, show me the future.")
