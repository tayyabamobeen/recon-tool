import whois

def run(domain):
    try:
        data = whois.whois(domain)
        return str(data)
    except Exception as e:
        return f"WHOIS Error: {e}"

