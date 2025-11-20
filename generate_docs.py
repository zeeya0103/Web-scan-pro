from reportlab.pdfgen import canvas # type: ignore

def generate_report(findings):
    c = canvas.Canvas("WebScanPro_Report.pdf")
    c.drawString(100, 800, "WebScanPro Vulnerability Report")
    
    y = 760
    for f in findings:
        c.drawString(50, y, "- " + f)
        y -= 20

    c.save()
    print("[+] Report Generated!")

findings = [
    "SQL Injection found at /sqli/",
    "XSS found at /xss/",
    "Weak credentials detected",
]

generate_report(findings)
