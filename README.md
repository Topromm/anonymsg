# Anonymsg

**Anonymsg** is a Discord bot designed to facilitate the sending of anonymous messages in a server. It allows users to express their thoughts anonymously, while still maintaining necessary moderation.

## Features
- **Anonymous Messaging**: Users can send messages anonymously to a pre-selected channel in the server using the `/sendanonymously` command.
- **Moderation Logging**: All anonymous messages are logged in a private staff channel, including message author details, for moderation and safety.
- **Customizable**: Admins can set which channels the bot sends anonymous messages to and where the logs are stored.

## Use Case Scenarios
- **Feedback and Suggestions**: Server members can offer constructive criticism or ideas while staying anonymous.
- **Sensitive Topics**: Members can discuss delicate matters privately and discreetly.


### Admin Commands (for server staff)
- `/load [extension]` — Loads the chosen extension.
- `/unload [extension]` — Unloads the chosen extension.
- `/reload [extension]` — Reloads the chosen extension.
- `/ping` — Checks the bot's current latency.
- `/send [message] [channel_id]` — Sends a message in the specified channel.
- `/sendhere [message]` — Sends a message in the current channel.
- `/dm [user] [message]` — Sends a DM to the chosen user.
- `/shutdown` — Shuts down the bot.
