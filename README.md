# 🔍 ReconTool – Modular Reconnaissance Tool (CLI Based)

A lightweight, modular reconnaissance tool for automated information gathering during penetration testing.

> Built with 💻 Python and 🐳 Docker. Supports both **Active** and **Passive** recon.

---

## 📌 Features

- ✅ **Passive Recon**
  - WHOIS Lookup
  - DNS Enumeration (A, MX, TXT, NS records)
  - Subdomain Enumeration via `crt.sh` API

- 🔥 **Active Recon**
  - Port Scanning (using `socket`)
  - Banner Grabbing
  - Technology Detection (via `whatweb` CLI)

- 📄 **Report Generation**
  - Output saved in `reports/report.txt`
  - Neatly structured with module-wise results
  - CLI-based flag control

---

## 🧱 Folder Structure


