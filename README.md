<p align="center">
  <img src="https://files.catbox.moe/eehxb4.jpg" alt="𝐓 - 𝐒𝐄𝐑𝐈𝐄𝐒 𝐌𝐔𝐒𝐈𝐂 Logo" width="300px">
</p>

<h1 align="center">˹𝐓 - 𝐒𝐄𝐑𝐈𝐄𝐒 𝐌𝐔𝐒𝐈𝐂˼</h1>

<p align="center"><b>Telegram Bot to Stream High-Quality Music in Voice Chats</b></p>

<p align="center">
  <a href="https://t.me/Botsyard">Support Channel</a> •
  <a href="https://t.me/Botsyard">Support Group</a> •
  <a href="https://t.me/WTF_WhyMeeh">Owner</a>
</p>

---

## 🚀 Features

- Stream music from **YouTube, Spotify, SoundCloud**
- **High-quality audio** in Telegram voice chats
- Clean UI and admin commands
- Playlist support & multi-language
- Easy deployment to **Render**, **Heroku**, or **VPS**

---

## 🛠️ Deployment

### Deploy to Render (Free Hosting)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Oxeigns/Tseries)

---

### Deploy to Heroku

[![Deploy to Heroku](https://img.shields.io/badge/Deploy%20to%20Heroku-purple?style=for-the-badge&logo=heroku)](https://dashboard.heroku.com/new?template=https://github.com/Oxeigns/Tseries)

---

### VPS Setup (Advanced)

```bash
sudo apt update && sudo apt install python3-pip ffmpeg git -y
git clone https://github.com/Oxeigns/Tseries
cd Tseries

python3 -m venv venv
source venv/bin/activate

pip install -U pip
pip install -r requirements.txt

cp sample.env .env
nano .env  # Add your API_ID, API_HASH, BOT_TOKEN, etc.

python3 -m Tseries
