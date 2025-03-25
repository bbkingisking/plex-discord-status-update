from flask import Flask, request
import json
import requests
import logging 
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DISCORD_USER_TOKEN = os.getenv('DISCORD_USER_TOKEN')
PLEX_USERNAME = os.getenv('PLEX_USERNAME')

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

def update_discord_status(status_text=None):
    """Update your Discord custom status. If status_text is None, clear the status."""
    discord_api_url = "https://discord.com/api/v9/users/@me/settings"
    headers = {
        "Authorization": DISCORD_USER_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {
        "custom_status": {
            "text": status_text if status_text else ""
        }
    }
    response = requests.patch(discord_api_url, headers=headers, json=payload)
    if response.status_code == 200:
        if status_text:
            print(f"Updated Discord status: {status_text}")
        else:
            print("Cleared Discord status")
    else:
        print(f"Failed to update Discord status: {response.text}")

@app.route('/plex-webhook', methods=['POST'])
def plex_webhook():
    # Check if the content type is multipart/form-data
    if request.content_type.startswith('multipart/form-data'):
        # Extract the payload field from the form data
        if 'payload' in request.form:
            try:
                # Parse the JSON payload
                payload = json.loads(request.form['payload'])

                # Specify user
                if payload['Account']['title'] == PLEX_USERNAME:

                    # Handle play/resume events
                    if payload['event'] in ['media.play', 'media.resume']:
                        # Check if the media type is a track (music)
                        if payload['Metadata']['type'] == 'track':
                            # Extract the song title and artist (grandparentTitle)
                            title = payload['Metadata']['title']
                            grandparent_title = payload['Metadata']['grandparentTitle']

                            # Update Discord status
                            status_text = f"🎵 Listening to {grandparent_title} - {title}"
                            update_discord_status(status_text)

                    # Handle pause/stop events
                    elif payload['event'] in ['media.pause', 'media.stop']:
                        # Clear Discord status
                        update_discord_status()  # No argument clears the status

            except Exception as e:
                print(f"Failed to process payload: {e}")
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5020)
