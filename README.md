# YouTube Video Uploader with Google API Integration

This project automates uploading videos to YouTube using the YouTube Data API v3. It features progress tracking, error logging, and customizable metadata like title, description, tags, and privacy status. Below, you'll find detailed setup instructions, including configuring the Google Cloud project.

---

## Features

- Authenticate with Google API using OAuth2.
- Upload videos to YouTube with a progress bar.
- Set metadata for videos: title, description, tags, privacy status, and category.
- Log errors in a file for debugging.
- Retry mechanism for upload failures.

---

## Prerequisites

1. **Python Installation**
   - Ensure Python 3.7+ is installed on your system.
   - Install `pip` (Python package manager) if not already available.

2. **Install Required Libraries**
   Run the following command to install the required dependencies:
   ```bash
   pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib tqdm
   ```

3. **Google Cloud Project Setup**
   - A Google Cloud project is required to access the YouTube Data API.

---

## Step-by-Step Setup

### 1. Enable the YouTube Data API

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project.
3. Navigate to **APIs & Services > Library**.
4. Search for "YouTube Data API v3" and click **Enable**.

### 2. Set Up OAuth 2.0 Credentials

1. In the **APIs & Services** menu, select **Credentials**.
2. Click **Create Credentials** > **OAuth 2.0 Client ID**.
3. Configure the consent screen:
   - Choose **External**.
   - Fill in app details (name, email, etc.).
   - Add "https://www.googleapis.com/auth/youtube.upload" and "https://www.googleapis.com/auth/youtube" as scopes.
4. Create credentials:
   - Application type: **Desktop App**.
   - Download the generated `client_secret.json` file and place it in the project directory.

### 3. Authenticate and Generate `token.json`

1. Run the script.
2. A browser will open for authentication.
3. Sign in with your Google account and allow access.
4. The generated `token.json` file will be saved in the project directory.

---

## How to Use

### 1. Run the Script

```bash
python script.py
```

### 2. Select the Video File

- A file dialog will open.
- Choose the video file you want to upload.

### 3. Input Metadata

- Enter a title, description, tags, privacy status, and category ID.
- Use defaults by pressing Enter.

### 4. Monitor Progress

- The progress bar will show upload progress.
- On success, the video ID will be printed.

---

## Code Breakdown

### Authentication

- The script uses `google-auth-oauthlib` to handle OAuth2 authentication.
- If a valid `token.json` exists, it reuses the credentials. Otherwise, it initiates a new authentication flow.

```python
def get_authenticated_service():
    ...
```

### Video Upload

- The `upload_video` function handles video upload, metadata setup, and error handling.
- A custom `ProgressFileUpload` class is used to track upload progress with `tqdm`.

```python
def upload_video(file, title, description, tags, category_id, privacy_status, game_title=None):
    ...
```

### Error Logging

- Errors during upload are logged in a file (`upload_errors.log`) for debugging.

```python
def log_error(error_message):
    ...
```

### Retry Mechanism

- Upload attempts are retried up to 3 times on failure.

---

## Google API Configuration Tips

1. **Scopes**:
   - Scopes define the level of access. This project uses:
     ```
     https://www.googleapis.com/auth/youtube.upload
     https://www.googleapis.com/auth/youtube
     ```

2. **Quota**:
   - Ensure sufficient quota for the YouTube Data API to avoid upload limits.

3. **Client Secrets**:
   - Keep `client_secret.json` secure. Never share it publicly.

---

## Example Metadata Input

- **Title**: `"My Valorant Highlights"`
- **Description**:
  ```
  #Valorant #GamingHighlights

  Subscribe for more awesome content!
  ```
- **Tags**: `"valorant, gameplay, highlights"`
- **Privacy Status**: `"public"`
- **Category ID**: `"20"` (Gaming)

---

## Logs and Debugging

- Errors are logged in `upload_errors.log` with timestamps.
- Use logs to troubleshoot issues such as invalid credentials, file not found, or API quota exceeded.

---

## Contributions

Feel free to suggest improvements or report bugs via [GitHub Issues](https://github.com/your-repo-link).

Happy uploading! 🚀