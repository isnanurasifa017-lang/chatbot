def get_bot_reply(message: str) -> str:
    text = message.lower()

    if "halo" in text or "hai" in text:
        return "Halo 👋 Selamat datang di Cookiebite 🍪"

    elif "jam buka" in text:
        return "🕘 Kami buka setiap hari pukul 09.00 – 21.00"

    elif "alamat" in text:
        return "📍 Jl. Ahmad Yani No.12, Tegal"

    elif "produk" in text:
        return (
            "🍪 Produk Cookiebite:\n"
            "- Chocolate Cookies\n"
            "- Cheese Cookies\n"
            "- Matcha Cookies"
        )

    elif "cara order" in text or "order" in text:
        return (
            "🛒 Cara Order:\n"
            "1. Ketik nama produk\n"
            "2. Tentukan jumlah\n"
            "3. Kirim alamat lengkap"
        )

    else:
        return (
            "Maaf 🙏 saya belum paham.\n"
            "Silakan tanya tentang jam buka, alamat, produk, atau cara order."
        )
