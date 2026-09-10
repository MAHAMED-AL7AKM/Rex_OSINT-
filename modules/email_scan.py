"""Rex OSINT - Email Scanner"""
import re, json, subprocess
from datetime import datetime
from config import GREEN, RED, YELLOW, BLUE, WHITE, RESET, RESULTS_DIR

def scan_email(email: str) -> dict:
    print(f"\n{BLUE}[*] Scanning email: {email}{RESET}")
    print(f"{BLUE}{'─' * 55}{RESET}")

    results = {"email": email, "checks": [], "dorks": []}

    # Validate format
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        print(f"{RED}[✗] Invalid email format{RESET}")
        return results
    print(f"{GREEN}[✓] Valid email format{RESET}")

    domain = email.split("@")[1]
    print(f"{GREEN}[✓] Domain: {domain}{RESET}")

    # Holehe (optional)
    print(f"\n{YELLOW}[*] Running Holehe (if installed)...{RESET}")
    try:
        r = subprocess.run(["holehe", email], capture_output=True, text=True, timeout=120)
        if r.returncode == 0:
            print(r.stdout)
            results["checks"].append({"tool": "holehe", "output": r.stdout})
    except FileNotFoundError:
        print(f"{YELLOW}[!] Holehe not installed. Run: pip install holehe{RESET}")
    except Exception as e:
        print(f"{RED}[✗] Holehe error: {e}{RESET}")

    # Dorks
    dorks = [
        f'"{email}"',
        f'"{email}" site:facebook.com',
        f'"{email}" site:linkedin.com',
        f'"{email}" site:github.com',
        f'"{email}" filetype:pdf',
    ]
    results["dorks"] = dorks
    print(f"\n{YELLOW}[*] Google Dorks:{RESET}")
    for d in dorks:
        print(f"   {WHITE}→ {d}{RESET}")

    return results