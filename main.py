import sys
from modules.passive import whois_lookup, dns_enum, subdomain_enum
from modules.active import port_scan, banner_grab, tech_detect
from modules import logger

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 main.py example.com --whois --dns --subdomains --ports --banner --tech")
        return

    domain = sys.argv[1]
    flags = sys.argv[2:]

    report_data = f"Recon Report for {domain}\n"
    report_data += "-" * 40 + "\n"

    if "--whois" in flags:
        report_data += "\n[WHOIS Lookup]\n"
        report_data += whois_lookup.run(domain) + "\n"

    if "--dns" in flags:
        report_data += "\n[DNS Enumeration]\n"
        report_data += str(dns_enum.run(domain)) + "\n"

    if "--subdomains" in flags:
        report_data += "\n[Subdomain Enumeration]\n"
        report_data += subdomain_enum.run(domain) + "\n"

    if "--ports" in flags:
        report_data += "\n[Port Scan]\n"
        report_data += port_scan.run(domain) + "\n"

    if "--banner" in flags:
        report_data += "\n[Banner Grabbing]\n"
        report_data += banner_grab.run(domain) + "\n"

    if "--tech" in flags:
        report_data += "\n[Technology Detection]\n"
        report_data += tech_detect.run(domain) + "\n"

    with open("reports/report.txt", "w") as file:
        file.write(report_data)

    print("\n✅ Report saved to reports/report.txt")

if __name__ == "__main__":
    main()

