import controllers.controller as controller

class Benedict(controller.Controller):
    async def process(self, params, message, client):
        await client.send_message(message.channel, "Battlefield Counterstrike")
