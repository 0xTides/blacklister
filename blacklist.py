import dns.resolver
import requests
import logging
import os

# Replace this URL with your own Slack webhook URL
SLACK_WEBHOOK_URL = ""

BLACKLISTS = [
    "zen.spamhaus.org",
    "dnsbl.sorbs.net",
    "bl.spamcop.net",
    "dnsbl-1.uceprotect.net",
    "dnsbl-2.uceprotect.net",
    "dnsbl-3.uceprotect.net",
    "db.wpbl.info",
    "b.barracudacentral.org",
    # Add more blacklists here
]

# Create a logs directory if it doesn't exist
LOGS_DIR = "logs"
if not os.path.exists(LOGS_DIR):
    os.mkdir(LOGS_DIR)

# Configure basic logging
logging.basicConfig(filename=f"{LOGS_DIR}/Blacklist.log", level=logging.INFO,
                    format="%(asctime)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

def check_ip_address(ip_address):
    blacklisted = []
    for blacklist in BLACKLISTS:
        try:
            # Perform the DNS lookup on the blacklist
            query = ".".join(reversed(str(ip_address).split("."))) + "." + blacklist
            answers = dns.resolver.resolve(query, "A")
            # If the DNS lookup returns a result, the IP address is blacklisted
            blacklisted.append(blacklist)
            print(f"\033[31mThe IP address {ip_address} is blacklisted on {blacklist}\033[0m")
        except dns.resolver.NXDOMAIN:
            # If the DNS lookup fails, the IP address is not blacklisted on this blacklist
            print(f"\033[32mThe IP address {ip_address} is not blacklisted on {blacklist}\033[0m")
            pass

    if blacklisted:
        logging.info(f"The IP address {ip_address} is blacklisted on the following blacklists: {', '.join(blacklisted)}")
    else:
        logging.info(f"The IP address {ip_address} is not blacklisted on any of the known blacklists.")

    return blacklisted

def send_slack_notification(ip_addresses, blacklists):
    message = "Blacklist check:\n"
    for i, ip_address in enumerate(ip_addresses):
        if blacklists[i]:
            message += f"- @here {ip_address} is blacklisted on the following blacklists: {', '.join(blacklists[i])}"
        else:
            message += f"- {ip_address} is not blacklisted on any of the known blacklists.\n"
    payload = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"```\n{message}\n```"
                }
            }
        ]
    }

    requests.post(SLACK_WEBHOOK_URL, json=payload)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ips', help='IP addresses to check, separated by commas')
    args = parser.parse_args()

    if args.ips:
        ip_addresses = args.ips.split(',')
    else:
        ip_addresses = input("Enter the IP addresses to check, separated by commas: ").split(',')

    blacklists = []
    for ip_address in ip_addresses:
        blacklisted = check_ip_address(ip_address.strip())
        blacklists.append(blacklisted)
        
    send_slack_notification(ip_addresses, blacklists)
