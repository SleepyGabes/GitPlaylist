# GitPlaylist
![Discord](https://img.shields.io/discord/1264696818240065697?style=for-the-badge&logo=Discord&label=CHAT&color=7289DA)

### Get started

- First things first, head on over to [Spotify for Developers](https://developer.spotify.com/) to create your app.

- Go to **Dashboard** and click **Create App**.

  ![Imgur](https://imgur.com/E7bQp97.png)

  ![Imgur](https://imgur.com/DgS9x23.png)

- Fill out this form to create your app.

  ![Imgur](https://imgur.com/NtRElCJ.png)

> For the "Redirect URI's", I don't think it actually matters what you put in there, but put my GitHub link in case you don't know what to put. "https://github.com/SleepyGabes/GitPlaylist".
> Also make sure you select "Web API".
> You should also read the Spotify's Developer Terms of Service and Design Guidelines, if you want to.

- Now click on your app and then go to **Settings**.

  ![Imgur](https://imgur.com/cNlUdIJ.png)

- Now you should see your **Client ID** and the option to show your **Client secret**.
> Note them somewhere on your desktop with notepad or something else, you will need them for later.

  ![Imgur](https://imgur.com/Ipnxes2.png)

- Now head on over to User Management and add yourself to the list.

  ![Imgur](https://imgur.com/DtGSAi3.png)

- Now download the latest version of GitPlaylist [here](https://github.com/SleepyGabes/GitPlaylist/releases/).

- In the `_interal` folder, you should find a `config.json` file, in there put your **Client ID** and **Client secret**.

- Now create a playlist on spotify and add a couple of songs you want to download and get the link of the spotify playlist.

- Now you need get the ID of the playlist, if don't know how click [this](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids).

- Now all you have to do is run the `GitPlaylist.exe` and your song's will start being downloaded here: `_internal/song_outputs`

- There may be an issue with my Py-to-exe program but if there is something wrong related to modules, run this in `cmd` inside of the folder: `pip install -r requirements.txt`
