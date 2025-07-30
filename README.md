# 📸 Capture-Écran - Outil de Capture Web Automatisée

**Créé par ozGod-sh**

## Description

Capture-Écran est un outil de reconnaissance web qui permet de prendre des captures d'écran automatisées de pages web via l'API ScreenshotOne. Idéal pour l'audit de sécurité, la surveillance de sites et la documentation de tests de pénétration.

## Fonctionnalités

### 📷 Capture avancée
- **API ScreenshotOne** : Service professionnel de capture d'écran
- **Page complète** : Capture de toute la page, pas seulement la partie visible
- **Blocage de publicités** : Supprime automatiquement les ads
- **Blocage de trackers** : Améliore la confidentialité et la vitesse
- **Timeout configurable** : Gestion des pages lentes

### 🛡️ Fonctionnalités de sécurité
- **Headers personnalisés** : User-Agent identifiable
- **Gestion d'erreurs** : Messages d'erreur détaillés
- **Validation d'entrée** : Vérification des paramètres
- **Sauvegarde locale** : Fichiers stockés localement

## Installation

### Prérequis
- Python 3.6+
- Compte ScreenshotOne (gratuit avec limitations)
- Clé API ScreenshotOne

### Installation des dépendances
```bash
cd Capture-Ecran
pip install -r requirements.txt
```

### Dépendances
- `requests` : Bibliothèque HTTP pour les appels API

### Obtenir une clé API
1. Visitez [screenshotone.com](https://screenshotone.com)
2. Créez un compte gratuit
3. Obtenez votre clé d'accès API
4. Plan gratuit : 100 captures/mois

## Utilisation

### Syntaxe de base
```bash
python capture_ecran.py -u <URL> -k <API_KEY> [OPTIONS]
```

### Options disponibles
- `-u, --url URL` : URL de la page à capturer (requis)
- `-k, --api-key KEY` : Clé d'accès API ScreenshotOne (requis)
- `-o, --output FICHIER` : Nom du fichier de sortie (défaut: screenshot.png)
- `-h, --help` : Affiche l'aide

### Exemples d'utilisation

#### 1. Capture basique
```bash
python capture_ecran.py -u "https://example.com" -k "votre_cle_api"
```

#### 2. Capture avec nom personnalisé
```bash
python capture_ecran.py -u "https://target.com" -k "votre_cle_api" -o "target_homepage.png"
```

#### 3. Capture de page de login
```bash
python capture_ecran.py --url "https://admin.example.com/login" --api-key "votre_cle_api" --output "login_page.png"
```## 
Structure des fichiers

```
Capture-Ecran/
├── capture_ecran.py    # Script principal
├── requirements.txt    # Dépendances Python
└── README.md          # Cette documentation
```

## Logique de fonctionnement

### 1. Configuration de l'API
```python
api_url = "https://api.screenshotone.com/take"
params = {
    'access_key': api_key,
    'url': url,
    'full_page': 'true',
    'block_ads': 'true',
    'block_trackers': 'true'
}
```

### 2. Appel API avec gestion d'erreurs
```python
response = requests.get(api_url, params=params, timeout=60)
if response.status_code == 200:
    with open(output_file, 'wb') as f:
        f.write(response.content)
```

### 3. Gestion des erreurs
- **Code 200** : Succès, sauvegarde de l'image
- **Autres codes** : Affichage du message d'erreur API
- **Timeout** : Gestion des pages qui ne répondent pas
- **Erreurs réseau** : Gestion des problèmes de connexion

## Cas d'usage

### Tests de pénétration
- **Reconnaissance passive** : Capturer les pages sans interaction
- **Documentation d'audit** : Preuves visuelles des vulnérabilités
- **Surveillance de changements** : Détecter les modifications de sites
- **Analyse de surface d'attaque** : Identifier les points d'entrée

### Développement web
- **Tests de régression visuelle** : Comparer les versions
- **Documentation** : Capturer l'état des applications
- **Monitoring** : Surveiller l'apparence des sites
- **Validation cross-browser** : Vérifier le rendu

### Investigation forensique
- **Preuves numériques** : Capturer l'état d'un site à un moment donné
- **Analyse de phishing** : Documenter les sites malveillants
- **Surveillance de marque** : Détecter les usurpations
- **Compliance** : Vérifier la conformité visuelle

## Paramètres API avancés

### Configuration actuelle
```python
params = {
    'access_key': api_key,
    'url': url,
    'full_page': 'true',        # Capture toute la page
    'block_ads': 'true',        # Bloque les publicités
    'block_trackers': 'true'    # Bloque les trackers
}
```

### Paramètres additionnels disponibles
- `viewport_width` : Largeur de la fenêtre (défaut: 1920)
- `viewport_height` : Hauteur de la fenêtre (défaut: 1080)
- `device_scale_factor` : Facteur d'échelle (défaut: 1)
- `format` : Format de sortie (png, jpg, webp)
- `quality` : Qualité JPEG (1-100)
- `delay` : Délai avant capture (secondes)
- `wait_for_selector` : Attendre un élément CSS
- `scroll_to_element` : Faire défiler vers un élément

## Exemple de sortie

### Succès
```
╔══════════════════════════════════════════════════════════╗
║                                                              ║
║  📸 Capture-Écran v1.0.0                                 ║
║                                                              ║
║  Prend des captures d'écran de pages web via une API.       ║
║  Créé par ozGod                                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════╝

[*] Demande de capture pour l'URL : https://example.com
[+] Capture d'écran enregistrée avec succès dans : screenshot.png
```

### Erreur
```
[*] Demande de capture pour l'URL : https://invalid-url.com
[!] Erreur de l'API (Code: 400): Invalid URL provided
```

## Gestion des erreurs courantes

### Erreurs API (ScreenshotOne)
- **400 Bad Request** : URL invalide ou paramètres incorrects
- **401 Unauthorized** : Clé API invalide ou expirée
- **402 Payment Required** : Quota dépassé
- **429 Too Many Requests** : Limite de taux dépassée
- **500 Internal Server Error** : Erreur du service

### Erreurs réseau
- **Timeout** : Page trop lente à charger
- **Connection Error** : Problème de connectivité
- **DNS Error** : Domaine inexistant

### Solutions
```bash
# Vérifier la clé API
curl "https://api.screenshotone.com/take?access_key=VOTRE_CLE&url=https://example.com"

# Tester la connectivité
ping api.screenshotone.com

# Vérifier le quota
# Connectez-vous à votre dashboard ScreenshotOne
```

## Alternatives et comparaisons

### Services similaires
- **Puppeteer** : Solution auto-hébergée avec Chrome headless
- **Selenium** : Automatisation de navigateur complète
- **wkhtmltopdf** : Conversion HTML vers PDF/image
- **PhantomJS** : Navigateur headless (déprécié)

### Avantages de ScreenshotOne
- **Pas d'installation** : Service cloud prêt à l'emploi
- **Optimisé** : Rendu rapide et fiable
- **Maintenance** : Pas de gestion d'infrastructure
- **Fonctionnalités** : Blocage d'ads, full page, etc.

### Inconvénients
- **Dépendance externe** : Nécessite une connexion Internet
- **Coût** : Limité par le quota
- **Confidentialité** : Les URLs sont envoyées au service
- **Personnalisation** : Moins flexible qu'une solution locale

## Sécurité et confidentialité

### ⚠️ Considérations importantes
- **URLs sensibles** : Éviter les URLs avec des tokens/secrets
- **Données privées** : Ne pas capturer de pages avec des informations sensibles
- **Logs du service** : ScreenshotOne peut logger les URLs
- **Stockage local** : Les captures sont sauvées localement

### Bonnes pratiques
```bash
# Utiliser des variables d'environnement pour la clé API
export SCREENSHOT_API_KEY="votre_cle_api"
python capture_ecran.py -u "https://example.com" -k "$SCREENSHOT_API_KEY"

# Nettoyer les captures sensibles après usage
rm -f sensitive_capture.png
```

## Intégration avec d'autres outils

### Scripts d'automatisation
```bash
#!/bin/bash
# Capturer plusieurs sites
sites=("https://site1.com" "https://site2.com" "https://site3.com")
for site in "${sites[@]}"; do
    python capture_ecran.py -u "$site" -k "$API_KEY" -o "$(basename $site).png"
done
```

### Avec des outils de reconnaissance
```bash
# Combiner avec subfinder pour capturer les sous-domaines
subfinder -d example.com | while read subdomain; do
    python capture_ecran.py -u "https://$subdomain" -k "$API_KEY" -o "${subdomain}.png"
done
```

### Monitoring automatisé
```python
import schedule
import time

def capture_daily():
    os.system('python capture_ecran.py -u "https://target.com" -k "API_KEY" -o "daily_$(date +%Y%m%d).png"')

schedule.every().day.at("09:00").do(capture_daily)
while True:
    schedule.run_pending()
    time.sleep(1)
```

## Limitations

### Techniques
- **JavaScript lourd** : Peut ne pas attendre le chargement complet
- **Authentification** : Ne gère pas les logins automatiques
- **Contenu dynamique** : Peut manquer le contenu chargé après la capture
- **Géolocalisation** : Capture depuis les serveurs de ScreenshotOne

### Quotas et limites
- **Plan gratuit** : 100 captures/mois
- **Taille d'image** : Limitée par le service
- **Timeout** : Maximum 60 secondes par capture
- **Formats** : PNG par défaut, autres formats selon le plan

## Améliorations futures

### Fonctionnalités
- Support de multiples services de capture
- Mode batch pour plusieurs URLs
- Configuration avancée des paramètres
- Intégration avec des bases de données

### Interface
- Interface graphique
- Mode interactif
- Configuration par fichier
- Logs détaillés

## Dépannage

### Problèmes courants
```bash
# Tester la clé API
python -c "import requests; print(requests.get('https://api.screenshotone.com/take?access_key=VOTRE_CLE&url=https://example.com').status_code)"

# Vérifier les dépendances
pip list | grep requests

# Tester avec curl
curl -o test.png "https://api.screenshotone.com/take?access_key=VOTRE_CLE&url=https://example.com&full_page=true"
```

## Licence

MIT License - Voir le fichier LICENSE pour plus de détails.

---

**Capture-Écran v1.0.0** | Créé par ozGod-sh