import socket

def run(domain):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((domain, 80))
        s.send(b"HEAD / HTTP/1.1\r\nHost: "+domain.encode()+b"\r\n\r\n")
        banner = s.recv(1024).decode()
        s.close()
        return banner
    except Exception as e:
        return f"Banner Grab Error: {e}"

