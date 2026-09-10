"""Rex OSINT - Banner"""
import os
from config import RED, MAGENTA, WHITE, YELLOW, BLUE, GREEN, RESET, VERSION

BANNER = f"""
{RED}
██████╗ ███████╗██╗  ██╗     ██████╗ ███████╗██╗███╗   ██╗████████╗
██╔══██╗██╔════╝╚██╗██╔╝    ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██████╔╝█████╗   ╚███╔╝     ██║   ██║███████╗██║██╔██╗ ██║   ██║
██╔══██╗██╔══╝   ██╔██╗     ██║   ██║╚════██║██║██║╚██╗██║   ██║
██║  ██║███████╗██╔╝ ██╗    ╚██████╔╝███████║██║██║ ╚████║   ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝
{MAGENTA}
        ▓▓▓  R E X   O S I N T   T O O L  ▓▓▓
        ═════════════════════════════════════════
            {WHITE}Professional Information Gathering
            {YELLOW}Version: {VERSION}  |  Author: {__import__('config').AUTHOR}
{MAGENTA}        ═════════════════════════════════════════
{BLUE}     [ Email ]  [ Phone ]  [ Username ]  [ Dorks ]
{RESET}
"""

def print_banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(BANNER)

def print_menu():
    print(f"""{BLUE}
    ┌──────────────────────────────────────────┐
    │              MAIN MENU                   │
    ├──────────────────────────────────────────┤
    │  {GREEN}[1]{WHITE} Email Scanner                       │
    │  {GREEN}[2]{WHITE} Phone Scanner                       │
    │  {GREEN}[3]{WHITE} Username Scanner                    │
    │  {GREEN}[4]{WHITE} Google Dorks Generator              │
    │  {GREEN}[5]{WHITE} Full Scan (All)                     │
    │  {GREEN}[6]{WHITE} View Saved Results                  │
    │  {RED}[0]{WHITE} Exit                                │
    └──────────────────────────────────────────┘
    """)