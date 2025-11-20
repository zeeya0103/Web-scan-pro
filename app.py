from auth_test import AuthTester
from crawler import run_crawler
from generate_docs import generate_report
from idor_test import IDORTester
from sqli_test import SQLInjectionTester 
from xss_test import XSSTester


def main():

    print("\n[+] Starting WebScanPro...\n")

    # 1️⃣ AUTHENTICATION TEST
    print("\n--- AUTH TEST ---")
    tester = AuthTester("http://localhost/dvwa/login.php")
    tester.brute_force()
    tester.session_test()

    # 2️⃣ CRAWLER
    print("\n--- CRAWLING TARGET ---")
    links = run_crawler()
    print(f"[+] Total links found: {len(links)}")

    # 3️⃣ SQL INJECTION TEST
    print("\n--- SQL INJECTION TEST ---")
    sql_tester = SQLInjectionTester(["http://localhost/dvwa/vulnerabilities/sqli/"])
    sql_results = sql_tester.test_sql()

    # 4️⃣ XSS TEST
    print("\n--- XSS TEST ---")
    xss_tester = XSSTester("http://localhost/dvwa/vulnerabilities/xss_r/")
    xss_results = xss_tester.test_xss()

    # 5️⃣ IDOR TEST
    print("\n--- IDOR TEST ---")
    idor = IDORTester("http://localhost/dvwa/vulnerabilities/idor/")
    idor_results = idor.test_idor()

    # 6️⃣ GENERATE REPORT
    print("\n--- GENERATING REPORT ---")

    findings = []
    findings.extend(sql_results)
    findings.extend(xss_results)
    findings.extend(idor_results)

    if not findings:
        findings.append("No vulnerabilities detected.")

    generate_report(findings)

    print("\n[+] Scan Complete! Report Saved as WebScanPro_Report.pdf\n")


if __name__ == "__main__":
    main()
