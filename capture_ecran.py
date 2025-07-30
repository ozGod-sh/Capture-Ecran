# -*- coding: utf-8 -*-
# Auteur: ozGod

import argparse
import requests
import sys

def display_banner():
    """Affiche une bannière stylisée pour l'outil."""
    VERSION = "1.0.0"
    AUTHOR = "ozGod"
    banner = f"""
╔══════════════════════════════════════════════════════════╗
║                                                              ║
║  📸 Capture-Écran v{VERSION}                                 ║
║                                                              ║
║  Prend des captures d'écran de pages web via une API.       ║
║  Créé par {AUTHOR}                                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════╝
"""
    print(banner)

def take_screenshot(url, api_key, output_file):
    """Prend une capture d'écran d'une URL en utilisant l'API ScreenshotOne."""
    api_url = "https://api.screenshotone.com/take"
    params = {
        'access_key': api_key,
        'url': url,
        'full_page': 'true',
        'block_ads': 'true',
        'block_trackers': 'true'
    }
    
    print(f"[*] Demande de capture pour l'URL : {url}")
    
    try:
        response = requests.get(api_url, params=params, timeout=60) # Timeout plus long pour les captures
        
        if response.status_code == 200:
            with open(output_file, 'wb') as f:
                f.write(response.content)
            print(f"[+] Capture d'écran enregistrée avec succès dans : {output_file}")
        else:
            error_message = response.json().get('message', response.text)
            print(f"[!] Erreur de l'API (Code: {response.status_code}): {error_message}", file=sys.stderr)
            sys.exit(1)
            
    except requests.RequestException as e:
        print(f"[!] Erreur de connexion à l'API : {e}", file=sys.stderr)
        sys.exit(1)

def main():
    display_banner()
    parser = argparse.ArgumentParser(
        description="Prend une capture d'écran d'une page web en utilisant l'API screenshotone.com.",
        epilog="Créé par ozGod. Vous devez obtenir une clé API gratuite sur screenshotone.com."
    )
    parser.add_argument("-u", "--url", required=True, help="L'URL de la page à capturer.")
    parser.add_argument("-k", "--api-key", required=True, help="Votre clé d'accès API de screenshotone.com.")
    parser.add_argument("-o", "--output", default="screenshot.png", help="Nom du fichier de sortie (par défaut: screenshot.png).")

    args = parser.parse_args()

    take_screenshot(args.url, args.api_key, args.output)

if __name__ == "__main__":
    main()
