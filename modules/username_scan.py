"""Rex OSINT - Username Scanner"""
import requests
from config import GREEN, RED, YELLOW, BLUE, WHITE, RESET

PLATFORMS = {
    "Facebook": "https://facebook.com/{}",
    "Instagram": "https://instagram.com/{}",
    "Twitter/X": "https://twitter.com/{}",
    "TikTok": "https://tiktok.com/@{}",
    "GitHub": "https://github.com/{}",
    "Reddit": "https://reddit.com/user/{}",
    "Pinterest": "https://pinterest.com/{}",
    "Telegram": "https://t.me/{}",
    "YouTube": "https://youtube.com/@{}",
    "Medium": "https://medium.com/@{}",
    "Twitch": "https://twitch.tv/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "LinkedIn": "https://linkedin.com/in/{}",
    "Behance": "https://behance.net/{}",
    "Dribbble": "https://dribbble.com/{}",
}

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def scan_username(username: str) -> dict:
    print(f"\n{BLUE}[*] Scanning username: {username}{RESET}")
    print(f"{BLUE}{'─' * 55}{RESET}")
    print(f"{YELLOW}[*] Checking {len(PLATFORMS)} platforms...{RESET}\n")

    found = []
    for name, url_template in PLATFORMS.items():
        url = url_template.format(username)
        try:
            r = requests.get(url, headers=HEADERS, timeout=8, allow_redirects=True)
            if r.status_code == 200:
                print(f"   {GREEN}[✓] {name}: FOUND → {url}{RESET}")
                found.append({"platform": name, "url": url})
            else:
                print(f"   {RED}[✗] {name}: not found{RESET}")
        except Exception:
            print(f"   {YELLOW}[?] {name}: connection error{RESET}")

    print(f"\n{GREEN}[✓] Total found: {len(found)}/{len(PLATFORMS)}{RESET}")
    return {"username": username, "found": found}