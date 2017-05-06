import controllers.controller as controller


class Members(controller.Controller):
    async def process(self, params, message, client):
        data = ""
        server = client.get_server(message.server.id)

        for member in server.members:
            data += "`" + str(member) + "`\n"

        await client.send_message(message.channel, data)
