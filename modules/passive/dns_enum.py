import dns.resolver

def run(domain):
    results = {}
    try:
        for record in ['A', 'MX', 'TXT', 'NS']:
            answers = dns.resolver.resolve(domain, record, raise_on_no_answer=False)
            results[record] = [ans.to_text() for ans in answers]
        return str(results)
    except Exception as e:
        return f"DNS Error: {e}"

