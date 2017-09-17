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