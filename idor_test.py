import requests

class IDORTester:
    def __init__(self, base_url):
        self.url = base_url

    def test_idor(self):
        print("[*] Testing IDOR...")
        for uid in range(1, 10):
            r = requests.get(self.url + f"?user={uid}")
            if "Unauthorized" not in r.text:
                print("[!] IDOR Possible – User:", uid)

idor = IDORTester("http://localhost/dvwa/vulnerabilities/idor/")
idor.test_idor()
