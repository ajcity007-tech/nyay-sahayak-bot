import os
import requests
import telebot

# -------------------------------------------------------------------
# Configuration - token is injected securely by GitHub Actions at runtime
# -------------------------------------------------------------------
TOKEN = os.environ.get("TELEGRAM_TOKEN")
if not TOKEN:
    raise EnvironmentError(
        "TELEGRAM_TOKEN environment variable is not set. "
        "Add it as a GitHub Secret (Settings -> Secrets -> Actions)."
    )

bot = telebot.TeleBot(TOKEN)

# Use the channel's @username exactly as it appears on Telegram
CHANNEL_ID = "@nyaysahayak_ai"

# -------------------------------------------------------------------
# Content generator - replace the body of this function with your real
# content source (RSS feed, API call, database query, etc.)
# -------------------------------------------------------------------
def fetch_legal_updates() -> str:
    """
    Returns the daily legal current affairs message.
    Customise this function to pull live content from any source you like.
    """
    update = (
        "⚖️ *Daily Legal Current Affairs – @nyaysahayak_ai*\n\n"
        "📌 *Supreme Court*\n"
        "• Landmark judgment updates from today's cause list.\n\n"
        "📌 *Legislative Updates*\n"
        "• Key amendments and bills tabled in Parliament.\n\n"
        "📌 *High Court Roundup*\n"
        "• Important orders from High Courts across India.\n\n"
        "📌 *Exam Relevance*\n"
        "• Key points for Judiciary / APO / CLAT PG aspirants.\n\n"
        "_Stay updated. Stay ahead._ 🇮🇳"
    )
    return update

# -------------------------------------------------------------------
# Broadcaster
# -------------------------------------------------------------------
def send_broadcast():
    try:
        message = fetch_legal_updates()
        bot.send_message(
            chat_id=CHANNEL_ID,
            text=message,
            parse_mode="Markdown",  # supports *bold*, _italic_, etc.
        )
        print("✅ Broadcast sent successfully to", CHANNEL_ID)
    except telebot.apihelper.ApiTelegramException as e:
        print(f"❌ Telegram API error: {e}")
        raise  # re-raise so GitHub Actions marks the run as failed
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        raise

# -------------------------------------------------------------------
# Entry point
# -------------------------------------------------------------------
if __name__ == "__main__":
    send_broadcast()
