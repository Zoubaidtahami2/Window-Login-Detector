 Windows Login Detector (Mini SOC Tool)

A Python-based security log analysis tool that detects suspicious authentication behavior from Windows Security logs.

Features
- Detect multiple failed logins (brute force attacks)
- Detect night-time logins (12AM–5AM)
- Generate CSV security report
- Works with exported Windows Security logs

Technologies Used
- Python
- CSV
- Windows Event Logs

Files
- detector.py → main analyzer script
- sample_logs.txt → dummy test logs
- report.csv → generated report

How to Run
```bash
python detector.py
