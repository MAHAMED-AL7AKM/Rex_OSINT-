#!/usr/bin/env python3
"""Rex OSINT - Main Entry Point"""
import os
import sys
import json
from datetime import datetime
from colorama import init

from config import VERSION, RESULTS_DIR, RED, GREEN, YELLOW, RESET
from modules.banner import print_banner, print_menu
from modules.email_scan import scan_email
from modules.phone_scan import scan_phone
from modules.username_scan import scan_username
from modules.dorks import generate_dorks

init(autoreset=True)

def save_results(data, target, scan_type):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe = target.replace("@", "_at_").replace("+", "").replace("/", "_")
    path = f"{RESULTS_DIR}/{scan_type}_{safe}_{ts}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"tool": "Rex OSINT", "version": VERSION, "timestamp": ts, "data": data},
                  f, ensure_ascii=False, indent=4)
    print(f"\n{GREEN}[✓] Saved: {path}{RESET}")

def view_results():
    print(f"\n{GREEN}[*] Saved Results:{RESET}")
    if not os.path.exists(RESULTS_DIR):
        print(f"{YELLOW}[!] No results directory yet{RESET}")
        return
    files = sorted(os.listdir(RESULTS_DIR))
    if not files:
        print(f"{YELLOW}[!] No saved results{RESET}")
    for i, f in enumerate(files, 1):
        print(f"  {GREEN}[{i}]{RESET} {f}")

def main():
    try:
        while True:
            print_banner()
            print_menu()
            choice = input(f"{YELLOW}  Rex@OSINT > {RESET}").strip()

            if choice == "1":
                email = input(f"\n{YELLOW}[?] Email address: {RESET}").strip()
                if email:
                    save_results(scan_email(email), email, "email")
            elif choice == "2":
                phone = input(f"\n{YELLOW}[?] Phone number (with country code, e.g. +2010...): {RESET}").strip()
                if phone:
                    save_results(scan_phone(phone), phone, "phone")
            elif choice == "3":
                u = input(f"\n{YELLOW}[?] Username: {RESET}").strip()
                if u:
                    save_results(scan_username(u), u, "username")
            elif choice == "4":
                generate_dorks()
            elif choice == "5":
                e = input(f"{YELLOW}[?] Email (or skip): {RESET}").strip()
                p = input(f"{YELLOW}[?] Phone (or skip): {RESET}").strip()
                u = input(f"{YELLOW}[?] Username (or skip): {RESET}").strip()
                if e: save_results(scan_email(e), e, "email")
                if p: save_results(scan_phone(p), p, "phone")
                if u: save_results(scan_username(u), u, "username")
            elif choice == "6":
                view_results()
            elif choice == "0":
                print(f"\n{RED}  Thanks for using Rex OSINT!{RESET}\n")
                sys.exit(0)
            else:
                print(f"{RED}[✗] Invalid option{RESET}")

            input(f"\n{YELLOW}[→] Press Enter to continue...{RESET}")
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Interrupted{RESET}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()