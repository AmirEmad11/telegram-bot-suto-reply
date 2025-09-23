# Telegram Userbot Project

## Overview
This is a Python Telegram userbot that automatically handles join requests to a Telegram channel and sends welcome messages to new users.

## Core Components
- **bot.py**: Main bot script using Telethon library
- **requirements.txt**: Python dependencies (telethon, pyTelegramBotAPI, telethon-patch)
- **Procfile.bin**: Process configuration for deployment

## Architecture
- Uses Telethon-patch (enhanced Telethon) for Telegram API interaction
- Monitors join requests using UpdatePendingJoinRequests events
- Automatically approves join requests and sends welcome messages
- Handles both pending requests and direct chat actions

## Configuration Required
Environment variables needed:
- TELEGRAM_API_ID: Your Telegram API ID from my.telegram.org
- TELEGRAM_API_HASH: Your Telegram API hash from my.telegram.org  
- TELEGRAM_PHONE: Your phone number for authentication
- TELEGRAM_CHANNEL: Target channel ID (default: -1001672479948)

## Deployment
- Runs as a worker process (not a web server)
- Uses VM deployment target for persistent operation
- No frontend component - console-only application