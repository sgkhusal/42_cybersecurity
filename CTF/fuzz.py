import requests

BASE_URL = "http://cybersec.42sp.org.br:3318/" 

ROUTES = [
    "admin", "backup", "config", "test", "login", "debug",
    "old", "secret", "server-status", "phpinfo", ".git",
    "database.sql", "dump", "dev", "console", "api"
]

def fuzz_urls():
    for route in ROUTES:
        url = f"{BASE_URL}/{route}"
        try:
            resp = requests.get(url, timeout=3)

            if resp.status_code == 200:
                print(f"[+] Found: {url} (200 OK)")
            elif resp.status_code in [301, 302]:
                print(f"[!] Redirect: {url} -> {resp.headers.get('Location')}")
            elif resp.status_code not in [404, 403]:
                print(f"[?] Other Response ({resp.status_code}) em {url}")

        except requests.RequestException as e:
            print(f"[-] Error accesing {url}: {e}")


if __name__ == "__main__":
    fuzz_urls()