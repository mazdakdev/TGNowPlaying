# TGNowPlaying

This repository contains a Python bot built using the Pyrogram library. The bot updates your Telegram channel's profile picture and name to display the music you are currently listening to from various music providers such as Spotify and Apple Music. The bot schedules updates every 5 minutes to ensure your channel is always showing the latest track.
Features


## Requirements

  - Python 3.7+
  - Telgram User API

## Preview

![preview](https://github.com/mazdakdev/TGNowPlaying/assets/60855141/7175df7a-c4be-4474-a80c-2ac5a32a79c7)
![terminal](https://github.com/mazdakdev/TGNowPlaying/assets/60855141/fadb2095-9a8a-481d-b7a4-4488bb7d5575)


## Deployment

1. Clone the repository:

      ```console
      user@host:~$ git clone https://github.com/mazdakdev/TGNowPlaying --depth=1
      ```
 2. Configure the Environment Variables:
       ```console
       user@host:~$ mv .env.sample .env && vim .env
       ```
   
3. Install Poetry using the official [Docs](https://python-poetry.org/docs/).

4.  Install the requirements and activate the virtual env's shell.

     ```console
     user@host:~$ poetry install && poetry shell
      ```


5. Run the Project

      ```console
      user@host:~$ bash start.sh
      ```


## Deployment with Docker 

  TODO:

## How to get Telegram User API
  TODO:

## Contributions

Contributions are, of course, welcome! Please open an issue or submit a pull request. For example, here is a step-by-step guide for adding a new provider:

1. Create an Adapter for Your Provider:
Navigate to the `adapters/` directory.
Create a new Python file for your service adapter, e.g., `your_service.py`.
Implement a class that inherits from `ProviderAdapter` and overrides the `fetch_current_item` method.

```python
from TGNowPlaying.adapters.base import ProviderAdapter
from typing import Optional, Tuple

class YourServiceAdapter(ProviderAdapter):
    def __init__(self):
        pass

    async def fetch_current_item(self) -> Optional[Tuple[str, str, str]]:
       title = do_sth_and_get_title()
       message = f"Currently doing {title}"
       image = do_sth_and_get_pfp()

       return title, message, image
```

2. Register Your Adapter in the Factory:
Open `factories/provider_factory.py`.
Add an entry for your service in the `_adapters` dictionary.

```python
class ProviderAdapterFactory:
    _adapters = {
        "spotify": SpotifyAdapter,
        "your_service": YourServiceAdapter,  # Add your service here
    }
    ....
```

3. Test and Submit a PR :)

## Happy Listening! 🎶


## TODO
- [ ] Docs
- [ ] Apple Music
- [ ] Vscode presence (like Discord)
