import os
import sys
import telebot

# ── Token Verification ─────────────────────────────────────────────────────
TOKEN = os.environ.get("TELEGRAM_TOKEN")
if not TOKEN:
    print("FATAL: TELEGRAM_TOKEN secret is missing or empty.")
    sys.exit(1)

# ── Target Channel Username ────────────────────────────────────────────────
CHANNEL_ID = "@nyaysahayak_ai"

# ── Initialize Bot ─────────────────────────────────────────────────────────
bot = telebot.TeleBot(TOKEN)

# ── Content Blueprint ──────────────────────────────────────────────────────
def fetch_legal_updates() -> str:
    return (
        "⚖️ *Daily Legal Current Affairs*\n"
        "📡 *Channel: @nyaysahayak_ai*\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🏛 *Supreme Court of India*\n"
        "• Today's landmark judgment highlights\n"
        "• Important constitutional bench updates\n\n"
        "📜 *Legislative Updates*\n"
        "• Key amendments tabled in Parliament\n"
        "• BNS / BNSS / BSA 2023 implementation news\n\n"
        "🏢 *High Court Roundup*\n"
        "• Significant orders across India\n\n"
        "📚 *Exam Relevance — Judiciary / APO / CLAT PG*\n"
        "• Key points for competitive law aspirants\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "_Stay updated. Stay ahead._ 🇮🇳\n"
        "*@nyaysahayak\\_ai* | Powered by @nyaysahayakbot"
    )

# ── Broadcast Execution ────────────────────────────────────────────────────
def send_broadcast():
    print(f"Attempting broadcast to channel: {CHANNEL_ID}")
    try:
        message = fetch_legal_updates()
        bot.send_message(
            chat_id=CHANNEL_ID,
            text=message,
            parse_mode="Markdown",
        )
        print("SUCCESS: Message successfully delivered to the channel.")
    except telebot.apihelper.ApiTelegramException as e:
        print(f"TELEGRAM API ERROR: {e}")
        print("\n💡 ACTIONABLE TROUBLESHOOTING CHECKLIST:")
        print("1. Open Telegram and go to your channel: @nyaysahayak_ai")
        print("2. Go to channel settings -> Administrators -> Add Administrator.")
        print("3. Search for exactly: @nyaysahayakbot")
        print("4. Make sure 'Post Messages' permission is switched ON.")
        raise
    except Exception as e:
        print(f"UNEXPECTED SYSTEM ERROR: {e}")
        raise

if __name__ == "__main__":
    send_broadcast()
