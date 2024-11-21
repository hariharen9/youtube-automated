import os
import time
import json
import tkinter as tk
from tkinter import filedialog
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from tqdm import tqdm  # Progress bar library

# Define constants
SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube",
    "https://www.googleapis.com/auth/youtube.force-ssl",
]

DEFAULT_TITLE = "RENAME"
DEFAULT_DESCRIPTION = """
#BadPanda #valorant #valorantclips #tamil #tamilgaming

Subscribe to BadPanda 🥳🥳
Join this channel to get access to perks:
https://www.youtube.com/channel/UCGRVM6oFyzOtGJxXH32ClBw/join
"""
DEFAULT_TAGS = [
        "valorant", "valorant ace", "valorant montage", "valorant best moments", 
        "ace valorant", "valorant pro", "fastest ace valorant", 
        "valorant best ace", "best ace valorant", "valorant ace sound", 
        "valorant fastest ace", "valorant ace complitation", 
        "valorant immortal", "best valorant plays", "radiant valorant", 
        "valorant aces", "valorant reflexes", "valorant reaction time", 
        "valo", "Valorant Moments", "Valorant Stream", "Valorant highlights", 
        "Valorant Platinums", "Valorant Ascendant", "tamil valorant", "tamil", "tamil gaming", "lo"
    ]
DEFAULT_GAME_TITLE = "Valorant"
DEFAULT_CATEGORY_ID = "20"
DEFAULT_PRIVACY_STATUS = "public"

CLIENT_SECRETS_FILE = "./client_secret.json"
TOKEN_FILE = "token.json"
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
LOG_FILE = "upload_errors.log"

def log_error(error_message):
    """Log error messages to a file."""
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {error_message}\n")

def open_file_dialog():
    """Open a file dialog to select a video file."""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv"), ("All Files", "*.*")]
    )
    return file_path

def get_authenticated_service():
    """Authenticate and create a YouTube API service."""
    credentials = None
    if os.path.exists(TOKEN_FILE):
        credentials = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as token:
            token.write(credentials.to_json())
    
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

def validate_category_id(category_id):
    """Validate if the category ID is numeric."""
    return category_id.isdigit()

def validate_privacy_status(privacy_status):
    """Validate if the privacy status is one of the allowed values."""
    return privacy_status in ["private", "public", "unlisted"]

def upload_video(file, title, description, tags, category_id, privacy_status, game_title=None):
    """Upload the video to YouTube with specified details and progress tracking."""
    youtube = get_authenticated_service()

    if isinstance(tags, str):
        tags = tags.split(",")

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id,
        },
        "status": {
            "privacyStatus": privacy_status,
        }
    }

    class ProgressFileUpload(MediaFileUpload):
        def __init__(self, filename, *args, **kwargs):
            super().__init__(filename, *args, **kwargs)
            self.total_size = os.path.getsize(filename)
            self.progress_bar = tqdm(
                total=self.total_size,
                unit="B",
                unit_scale=True,
                desc="Uploading",
                ncols=100,
            )
            self.bytes_uploaded = 0

        def next_chunk(self, *args, **kwargs):
            chunk = super().next_chunk(*args, **kwargs)
            if chunk[0]:
                uploaded = int(chunk[0].progress() * self.total_size)
                self.progress_bar.update(uploaded - self.bytes_uploaded)
                self.bytes_uploaded = uploaded
            return chunk

        def __del__(self):
            try:
                self.progress_bar.close()
            except Exception as e:
                log_error(f"Progress bar closing error: {str(e)}")

    media = ProgressFileUpload(file, chunksize=1024 * 1024, resumable=True)

    for attempt in range(3):  # Retry mechanism with 3 attempts
        try:
            request = youtube.videos().insert(
                part="snippet,status",
                body=body,
                media_body=media,
            )
            response = request.execute()
            print("\nVideo uploaded successfully! Video ID:", response.get("id"))

            if game_title:
                video_id = response.get("id")
                youtube.videos().update(
                    part="snippet",
                    body={
                        "id": video_id,
                        "snippet": {
                            "categoryId": category_id,
                            "defaultLanguage": "en",
                            "title": title,
                            "description": description,
                            "tags": tags,
                            "liveBroadcastContent": "none",
                            "gameTitle": game_title,
                        }
                    }
                ).execute()
                print("Game title updated successfully!")
            return
        except HttpError as e:
            error_message = f"Attempt {attempt + 1}: {str(e)}"
            print(error_message)
            log_error(error_message)
            if attempt < 2:
                print("Retrying upload...")
            time.sleep(2)
    print("Upload failed after 3 attempts.")

def main():
    video_file = open_file_dialog()
    if not video_file:
        print("No file selected. Exiting.")
        return

    title = input("Enter the video title: ").strip() or DEFAULT_TITLE
    description = input("Enter the video description (or press Enter for default): ").strip() or DEFAULT_DESCRIPTION
    tags_input = input("Enter comma-separated tags (or press Enter for defaults): ").strip()
    tags = tags_input.split(",") if tags_input else DEFAULT_TAGS

    category_id = input(f"Enter category ID (default: {DEFAULT_CATEGORY_ID}): ").strip() or DEFAULT_CATEGORY_ID
    while not validate_category_id(category_id):
        print("Invalid category ID. Please enter a numeric value.")
        category_id = input("Enter category ID: ").strip()

    privacy_status = input(f"Enter privacy status (private, public, unlisted; default: {DEFAULT_PRIVACY_STATUS}): ").strip() or DEFAULT_PRIVACY_STATUS
    while not validate_privacy_status(privacy_status):
        print("Invalid privacy status. Please enter 'private', 'public', or 'unlisted'.")
        privacy_status = input("Enter privacy status: ").strip()

    game_title = input(f"Enter the game title (default: {DEFAULT_GAME_TITLE}): ").strip() or DEFAULT_GAME_TITLE

    upload_video(video_file, title, description, tags, category_id, privacy_status, game_title)

if __name__ == "__main__":
    main()
