"""Rex OSINT - Phone Scanner"""
from config import GREEN, RED, YELLOW, BLUE, MAGENTA, WHITE, RESET

def scan_phone(phone: str) -> dict:
    print(f"\n{BLUE}[*] Scanning phone: {phone}{RESET}")
    print(f"{BLUE}{'─' * 55}{RESET}")

    results = {"phone": phone, "info": {}, "links": {}, "dorks": []}

    try:
        import phonenumbers
        from phonenumbers import geocoder, carrier, timezone

        parsed = phonenumbers.parse(phone, None)
        if not phonenumbers.is_valid_number(parsed):
            print(f"{RED}[✗] Invalid phone number{RESET}")
            return results

        info = {
            "country": geocoder.description_for_number(parsed, "en"),
            "carrier": carrier.name_for_number(parsed, "en"),
            "timezone": list(timezone.time_zones_for_number(parsed)),
            "international": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
        }
        results["info"] = info

        for key, val in info.items():
            print(f"{GREEN}[✓] {key.title()}: {val}{RESET}")
    except ImportError:
        print(f"{YELLOW}[!] phonenumbers not installed{RESET}")
    except Exception as e:
        print(f"{RED}[✗] Error: {e}{RESET}")

    links = {
        "Truecaller": f"https://www.truecaller.com/search/eg/{phone}",
        "Sync.me": f"https://sync.me/search/?number={phone}",
        "WhatsApp": f"https://wa.me/{phone}",
        "Telegram": f"https://t.me/{phone}",
    }
    results["links"] = links
    print(f"\n{YELLOW}[*] Direct Lookup Links:{RESET}")
    for name, link in links.items():
        print(f"   {MAGENTA}• {name}: {WHITE}{link}{RESET}")

    dorks = [
        f'"{phone}"',
        f'"{phone}" site:facebook.com',
        f'"{phone}" filetype:pdf',
    ]
    results["dorks"] = dorks
    print(f"\n{YELLOW}[*] Google Dorks:{RESET}")
    for d in dorks:
        print(f"   {WHITE}→ {d}{RESET}")

    return results