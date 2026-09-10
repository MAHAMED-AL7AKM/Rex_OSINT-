"""Rex OSINT - Google Dorks Generator"""
from config import GREEN, YELLOW, BLUE, WHITE, RESET

DORK_TEMPLATES = {
    "1": ("Person Name", [
        '"{t}"',
        '"{t}" site:facebook.com',
        '"{t}" site:linkedin.com',
        '"{t}" filetype:pdf',
        '"{t}" (CV OR resume OR سيرة)',
    ]),
    "2": ("Email", [
        '"{t}"',
        '"{t}" site:pastebin.com',
        '"{t}" filetype:pdf',
        'site:github.com "{t}"',
    ]),
    "3": ("Phone", [
        '"{t}"',
        '"{t}" site:facebook.com',
        '"{t}" (whatsapp OR telegram)',
    ]),
    "4": ("Domain", [
        'site:{t}',
        'site:{t} filetype:pdf',
        'site:{t} inurl:admin',
        'site:{t} intitle:index of',
    ]),
    "5": ("Username", [
        '"{t}"',
        '"@{t}"',
        'site:github.com "{t}"',
    ]),
}

def generate_dorks():
    print(f"\n{BLUE}[*] Google Dorks Generator{RESET}")
    print(f"{BLUE}{'─' * 55}{RESET}")
    print(f"{YELLOW}Select type:{RESET}")
    for k, (name, _) in DORK_TEMPLATES.items():
        print(f"  {GREEN}[{k}]{WHITE} {name}")

    choice = input(f"\n{YELLOW}  > {RESET}").strip()
    if choice not in DORK_TEMPLATES:
        print(f"{YELLOW}[!] Invalid choice{RESET}")
        return

    target = input(f"{YELLOW}[?] Enter target: {RESET}").strip()
    if not target:
        return

    _, templates = DORK_TEMPLATES[choice]
    print(f"\n{GREEN}[✓] Generated Dorks:{RESET}")
    print(f"{BLUE}{'─' * 55}{RESET}")
    for t in templates:
        print(f"  {WHITE}{t.format(t=target)}{RESET}")
    print(f"{BLUE}{'─' * 55}{RESET}")