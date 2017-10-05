Just install the dependencies from the `dependencies.txt` file, and you're almost good to go.

There's just one little thing. You have to create a file called `config.py` in the root of the project and create
this variables in it. Then you're good to go.

```python
# for ssh.py
SSH_SERVER_IP = "ssh server ip address"
SSH_SERVER_USERNAME = "ssh server username"
SSH_SERVER_PASSWORD = "ssh server password"

# for spotify.py
SPOTIFY_CLIENT_ID = "spotify client id"
SPOTIFY_CLIENT_SECRET = "spotify client secret"

# bot id, without this, bot will not run
BOT_ID = "bot id"
```

To add this bot to server, fill your bot's id to this link and change permissions (calculator here: `https://discordapi.com/permissions.html`):

`https://discordapp.com/oauth2/authorize?&client_id=<BOT_ID>&scope=bot&permissions=<PERMISSIONS>`


If you want to use deploy script, create `deploy.sh`. Here is example:

```bash
rm output.zip
zip -r output.zip * -x "output.zip"
scp -i <path_to_your_aws_pem_file> output.zip <username>@<ip>:~/discord_bot.zip
ssh -i <path_to_your_aws_pem_file> username@<ip> "sudo rm -rf ~/discord_bot; mkdir ~/discord_bot; unzip discord_bot.zip -d ~/discord_bot; sudo systemctl restart discord_bot.service;"
```

This deploy script uses linux services to run. You can find instructions here:

`http://www.diegoacuna.me/how-to-run-a-script-as-a-service-in-raspberry-pi-raspbian-jessie/`