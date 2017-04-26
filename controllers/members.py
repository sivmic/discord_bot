import controllers.controller as controller


class Members(controller.Controller):
    async def process(self, params, channel, client):
        members = ""

        for server in client.servers:
            for member in server.members:
                members += str(member) + "\n"

        await client.send_message(channel, members)
