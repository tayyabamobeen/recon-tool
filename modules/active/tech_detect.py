import subprocess

def run(domain):
    try:
        result = subprocess.check_output(['whatweb', domain], stderr=subprocess.DEVNULL)
        return result.decode()
    except Exception as e:
        return f"Tech Detection Error: {e}"

