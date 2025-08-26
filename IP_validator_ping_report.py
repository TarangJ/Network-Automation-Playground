import ipaddress
import subprocess
import json

from IP_Validation import valid_ips, invalid_ips


def ping_host(ip):
    try:
        result = subprocess.run(
            ["ping", "-t", "1" , ip],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            timeout = 3
        )
        if result.returncode == 0:
            ping_status = f"{ip} is UP"
        else:
            ping_status = f"{ip} is Down"

        print(f"Ping Status : ",ping_status)

    except subprocess.TimeoutExpired:
        return False


def main():
    with open ('ip.text', 'r') as f:
        ips = f.read().splitlines()

    report = {"valid": [], "invalid": []}

    for ip in ips:
        try:
            ipaddress.ip_address(ip)
            status = "alive" if ping_host(ip) else "dead"
            report["valid"].append({"ip ": ip, "status ": status})
        except Exception:
            report["invalid"].append(ip)

    with open('report.json', 'w') as f:
        json.dump(report ,f, indent=4)


    print("Report saved to report.json")


if __name__ == "__main__"  :
    main()

