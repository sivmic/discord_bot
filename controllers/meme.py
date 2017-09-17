import controllers.controller as controller


class Meme(controller.Controller):
    async def process(self, params, message, client):
        await client.delete_message(message)
