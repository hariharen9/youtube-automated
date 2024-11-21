# 🎥 YouTube Video Uploader with Google API Integration 🚀

Automate your YouTube video uploads like a pro! This project leverages the **YouTube Data API v3** to simplify video uploads, complete with progress tracking, error logging, and customizable metadata. Whether you're a creator or just someone who loves automation, this tool has you covered. 😎

---

## ✨ Features ✨

- 🔒 **Authenticate** with Google API using OAuth2 (upload to any account seamlessly!).  
- 📤 **Upload videos** to YouTube effortlessly.  
- 📝 **Set metadata** for videos: title, description, tags, privacy status, and category—or go default for speed!  
- 🛠️ **Log errors** in a file for easy debugging.  
- 🔄 **Retry failed uploads** up to three times, so you never miss a beat.

---

## 🛠️ Prerequisites 🛠️

1. **🐍 Python Installation**  
   - Make sure Python 3.7+ is installed.  
   - Install `pip` (Python package manager) if you don't have it.  

2. **📦 Install Required Libraries**  
   Run this magical command to get started:  
   ```bash
   pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib tqdm
   ```

3. **🌩️ Google Cloud Project Setup**  
   - A Google Cloud project is your gateway to the YouTube Data API.

---

## 🧙‍♂️ Step-by-Step Wizardry 🧙‍♀️

### 1️⃣ Enable the YouTube Data API 🛠️

1. Visit the [Google Cloud Console](https://console.cloud.google.com/) 🌐.  
2. Create a new project or select an existing one. 📁  
3. Go to **APIs & Services > Library** 📚.  
4. Search for **"YouTube Data API v3"** 🔍 and click **Enable** ✅.

---

### 2️⃣ Set Up OAuth 2.0 Credentials 🔐

1. In the **APIs & Services** menu, select **Credentials**.  
2. Click **Create Credentials** > **OAuth 2.0 Client ID**.  
3. Configure the consent screen:  
   - Choose **External** 🌍.  
   - Fill in app details (name, email, etc.).  
4. Create credentials:  
   - Application type: **Desktop App** 💻.  
   - Download the shiny new `client_secret.json` file and place it in your project directory.

---

### 3️⃣ Authenticate and Generate `token.json` 🪄

1. Run the script 🏃‍♂️.  
2. A browser will open, asking you to sign in with your Google account. 🌟  
3. Allow the requested permissions. 👍  
4. A `token.json` file will magically appear in your project directory. 🎉

---

## 🚀 How to Use This Wizardry

### 🏃‍♀️ 1. Run the Script

```bash
python script.py
```

### 📂 2. Select Your Video File

- A file dialog will pop up. 🖼️  
- Choose the video file you want to upload (don’t forget where you saved it!).  

### 🖊️ 3. Customize or Default Metadata  

- Enter the video title, description, tags, privacy status, and category ID.  
- Want a quick upload? Just hit Enter to use the default settings. 🚀  

### 🎬 4. Watch the Magic  

- The progress bar will show the upload status. 🟦⬜⬜⬜  
- On success, your video ID will be displayed. 💃

---

## 💡 Google API Configuration Tips 🔧

1. **✨ Scopes**:  
   - Permissions define your API's superpowers! This project uses:  
     ```
     https://www.googleapis.com/auth/youtube.upload
     https://www.googleapis.com/auth/youtube
     https://www.googleapis.com/auth/youtube.force-ssl
     ```

2. **📊 Quota**:  
   - Ensure you have enough quota for uploads to avoid hitting limits.  

3. **🔒 Security**:  
   - Keep `client_secret.json` safe! Sharing it is like giving away the keys to your house! 🏠

---

## 🤖 Default Metadata Suggestions

**Title**: `"My Amazing Gaming Highlights"` 🎮  
**Description**:  
```
#Valorant #GamingHighlights

Don't forget to like and subscribe for more awesome videos! 💕
```  
**Tags**: `"valorant, gaming, highlights, fun"` 🏆  
**Privacy Status**: `"public"` 🌍  
**Category ID**: `"20"` (Gaming) 🎲  

💡 **Pro Tip**: Customize the defaults in the code to save time!

---

## 🐞 Logs and Debugging 🛠️

- All errors are logged in `upload_errors.log` 📜, complete with timestamps.  
- Perfect for troubleshooting things like invalid credentials or API limits. 🧐  

---

## 🤝 Contributions Welcome!

Got ideas for improvement or found a bug? 🐛  
Let us know via [GitHub Issues](https://github.com/your-repo-link)!  

Let’s make this tool even more awesome together! 💪  

---

**🎉 Happy Uploading! 🎉**  
