import requests

def run(domain):
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        r = requests.get(url, timeout=10)
        data = r.json()
        subdomains = set()
        for entry in data:
            subdomains.add(entry['name_value'])
        return "\n".join(subdomains)
    except Exception as e:
        return f"Subdomain Error: {e}"

