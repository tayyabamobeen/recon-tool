import socket

def run(domain):
    open_ports = []
    ports = [21, 22, 23, 80, 443, 8080]
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((domain, port))
            open_ports.append(port)
            s.close()
        except:
            continue
    return f"Open Ports: {open_ports}"

