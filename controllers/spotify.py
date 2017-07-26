import controllers.controller as controller
import spotipy
import spotipy.oauth2 as oauth
import requests
import io


class Spotify(controller.Controller):
    async def process(self, params, message, client):
        spotify_client = oauth.SpotifyClientCredentials(client_id="561ac60138d44c1fa07ad222fc7ae523",
                                                        client_secret="aa3e17db5b7f42da8097c0f956821bc3")

        uri = ' '.join(params)

        spotify = spotipy.Spotify(client_credentials_manager=spotify_client)
        result = spotify.track(uri)

        band_name = result["album"]["artists"][0]["name"]
        song_name = result["name"]
        picture_url = result["album"]["images"][2]["url"]
        picture = requests.get(picture_url)

        data = "**" + song_name + "** by **" + band_name + "**"
        data += "\n" + uri.strip() + ""
        sent_by = "Sent by: **" + str(message.author.nick) + "**"

        await client.delete_message(message)
        await client.send_message(message.channel, data)
        await client.send_file(message.channel, io.BytesIO(picture.content), filename="thumbnail.png")
        await client.send_message(message.channel, sent_by)
