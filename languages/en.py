S = {
    "greet_morning": "Good morning 🌞",
    "greet_afternoon": "Good afternoon 🌤",
    "greet_evening": "Good evening 🌆",
    "greet_night": "Good night 🌙",
    "start_txt": (
        "<b>👋 Hey {name}, {greet}!</b>\n\n"
        "<b>🎬 Movies • 📺 Web Series • 🍥 Anime</b>\n"
        "<b>⚡ Fast search • Smart filter</b>\n\n"
        "<b>📝 Just send me a movie name — I'll find it!</b>\n\n"
        "<b>🔔 Latest updates:</b> {updates}\n"
        "<b>✦ Powered by @NeonGhost_Network</b>"
    ),
    "help_txt": (
        "<b>📖 HOW TO USE</b>\n\n"
        "<b>1️⃣ Check the correct name on Google</b>\n"
        "<b>2️⃣ Send that name here or in the group</b>\n"
        "<b>3️⃣ Use these formats:</b>\n\n"
        "<b>🎬 Movie:</b> name + year (e.g. Joker 2019)\n"
        "<b>📺 Series:</b> name + S01 (S01 = season 1)\n"
        "<b>🗣 Language:</b> name + Hindi\n\n"
        "<b>🚀 Follow these steps and get your file!</b>"
    ),
    "about_txt": (
        "<b>🤖 ABOUT ME</b>\n\n"
        "<b>• Name:</b> <a href=\"https://t.me/{bot_user}\">{bot_name}</a>\n"
        "<b>• Developer:</b> <a href=\"{owner}\">Owner</a>\n"
        "<b>• Library:</b> Pyrogram\n"
        "<b>• Language:</b> Python 3\n"
        "<b>• Database:</b> MongoDB\n"
        "<b>• Server:</b> Heroku"
    ),
    "btn_add_group": "➕ Add me to your group",
    "btn_help": "📖 Help",
    "btn_about": "ℹ️ About",
    "btn_top": "🔥 Top searches",
    "btn_premium": "💎 Premium",
    "btn_language": "🌐 Language",
    "btn_admin": "🛠 Admin Panel",
    "btn_back_home": "⬅️ Back to home",
    "btn_close": "❌ Close",
    "lang_saved": "✅ Language saved!",
}

S.update({'limit_reached': '<b>🚫 DAILY LIMIT REACHED</b>\n\n<b>📦 Free users get {limit} files per day.</b>\n\n<b>Choose one to continue 👇</b>\n<b>🔓 Verify</b> — free access for <b>{hours} hours</b>\n<b>💎 Premium</b> — unlimited, no verification', 'btn_verify': '🔓 Verify • Free {hours}h', 'remaining_txt': '<b>📦 Files left today: {left}/{total}</b>', 'del_notice': '<b>⏳ AUTO-DELETE</b>\n<b>This file will be deleted in {time}.</b>\n<b>📥 Download or save it before that.</b>', 'fwd_locked': '<b>🔒 Forwarding is off for free users.</b>\n<b>🔓 Verify or 💎 get Premium to unlock it.</b>', 'deleted_notice': '<b>🗑 File deleted. Search again anytime 😉</b>', 'verify_intro': '<b>🔓 FREE VERIFICATION</b>\n\n<b>1️⃣ Tap “Verify now”</b>\n<b>2️⃣ Complete the page and come back</b>\n<b>3️⃣ Enjoy {hours} hours of unlimited files + forwarding!</b>\n\n<b>❓ Stuck? Tap “How to verify”.</b>', 'btn_verify_now': '✅ Verify now', 'btn_how_to': '🎬 How to verify', 'verify_success': '<b>✅ VERIFIED!</b>\n\n<b>🎉 Unlimited files + forwarding are ON</b>\n<b>⏰ Till {until}</b>', 'btn_get_file': '📥 Get my file', 'verify_fast': '<b>⚠️ Verification failed</b>\n<b>Please open the link, complete the page properly and try again.</b>', 'verify_expired': '<b>⌛ This link has expired. Tap Verify again.</b>', 'verify_unavailable': '<b>🔧 Verification is not available right now.</b>\n<b>💎 Get Premium to continue.</b>', 'verify_active': '<b>✅ You are already verified till {until}.</b>', 'unit_h': 'h', 'unit_m': 'm'})

S.update({'no_file': '<b>❌ File not found. Please search again.</b>'})
