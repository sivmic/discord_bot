import controllers.controller as controller


class Lunch(controller.Controller):
    async def process(self, params, message, client):
        await client.delete_message(message)
        await client.send_message(message.channel, "Gideon, what's for lunch?")
