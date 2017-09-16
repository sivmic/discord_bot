import controllers.controller as controller
from pexpect import pxssh

HOSTNAME = "89.203.249.44"
USERNAME = "root"
PASSWORD = "58FNMo15"

commands = {
    "instances": "ps -aux | grep python | wc -l",
    "locked": "cat gajdosoci_script/nohup.out | grep locked | wc -l",
    "records": "cat gajdosoci_script/nohup.out | grep Instance | wc -l"
}


class Ssh(controller.Controller):
    async def process(self, params, message, client):
        user_input = ' '.join(params)
        command = commands[user_input]

        ssh_output = ""

        ssh = pxssh.pxssh()
        if ssh.login(HOSTNAME, USERNAME, PASSWORD, login_timeout=10):
            ssh.sendline(command)
            if ssh.prompt(1):
                ssh_output = ssh.before
            ssh.logout()

        ssh_output = ssh_output.decode('utf-8')

        data = ""
        if ssh_output != "":
            data = ssh_output.replace(command, "")
            data = ''.join(filter(lambda x: x.isdigit(), data))

        if user_input == "instances":
            data = str(int(data) - 1)

        data = "**" + user_input + "**: " + data

        await client.delete_message(message)
        await client.send_message(message.channel, data)
