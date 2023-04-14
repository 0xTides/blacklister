This python tool checks if an IP address is blacklisted on known blacklists. This tool can help you quickly identify if your IP address is blacklisted and notify you through a Slack channel.

To use this tool, simply run the code in the Python environment and provide the IP addresses you want to check. You can do this by passing the IP addresses as a command-line argument or by inputting them when prompted.

The tool will then check each IP address against a list of known blacklists and report which ones it is blacklisted on. If an IP address is blacklisted, the tool will send a notification to your Slack channel.

To use the Slack notification feature, you will need to replace the SLACK_WEBHOOK_URL variable in the code with your own Slack webhook URL.

------

1. Clone or download the repository to your local machine.

2. Make sure you have Python 3.x installed on your machine.

3. Open a terminal or command prompt and navigate to the directory where the repository is located.

4. Install the required packages by running the following command:

5. pip install -r requirements.txt
This will install the dns.resolver and requests packages that the tool depends on.

6. Open the blacklister.py file in your preferred text editor.

7. Replace the SLACK_WEBHOOK_URL variable with your own Slack webhook URL.

8. Save the file and close the text editor.

9. In the terminal or command prompt, run the following command:

python blacklist_checker.py -i <ip_address1>,<ip_address2>,<ip_address3>,...
Replace <ip_address1>,<ip_address2>,<ip_address3>,... with the IP addresses you want to check, separated by commas.

Alternatively, you can run the command without the -i option, and the tool will prompt you to enter the IP addresses.

Wait for the tool to finish checking the IP addresses. The tool will output which blacklists each IP address is blacklisted on.

If any of the IP addresses are blacklisted, the tool will send a notification to your Slack channel.
