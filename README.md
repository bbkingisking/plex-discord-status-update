# Plex to Discord Status Sync

A Flask app that updates your Discord custom status based on Plex media playback activity. Automatically displays the currently playing music track and clears the status when paused or stopped.

## Features

- 🎧 Syncs Plex music playback with Discord status
- 🚀 Automatic status updates for play/resume events
- 🧹 Automatic status clearing for pause/stop events
- 🔒 Secure token management using environment variables

## Requirements

- Python 3.6+
- Plex Media Server with webhooks enabled
- Discord account
- Server/PC with port 5020 accessible (or port forwarding configured)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bbkingisking/plex-discord-status-sync.git
   cd plex-discord-status-sync
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Environment file config**
   - Create a `.env` file in the project directory
   - Add your Discord user token:
     ```env
     DISCORD_USER_TOKEN=your_discord_user_token_here
     ```
   - Add your Plex username:
     ```env
     PLEX_USERNAME=your_plex_username_here
     ```

2. **Plex Webhook Setup**
   - Open Plex Web interface
   - Go to Settings → Webhooks
   - Add a new webhook with URL: `http://your-server-ip:5020/plex-webhook`

## Usage

1. Start the server:
   ```bash
   python main.py
   ```

2. Play music in Plex to test:
   - Status should update to: `🎵 Listening to Artist - Song Title`
   - Pausing/stopping will clear the status

## Troubleshooting

- Check server console for errors
- Verify webhook URL in Plex settings
- Ensure port 5020 is open in firewall/security groups
- Confirm Discord token is valid
- Confirm Plex username is entered correctly (may be case sensitive)
- Check Plex server logs for webhook delivery attempts

## Example Output

When playing music:
```plaintext
Updated Discord status: 🎵 Listening to Bob Dylan - Desolation Row
```
