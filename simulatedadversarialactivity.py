#!/usr/bin/python3

# Simulate Adversarial Activity
# Cyber Guardians
# 05/15/23

# Main

import random
import time
from datetime import datetime

# Define the log file (replace this with your log file path)
log_file = 'your_log_file.log'

# Define a list of simulated IP addresses
ip_addresses = ['123.45.67.89', '98.76.54.32', '192.168.1.2', '10.0.0.1']

# Define a list of user names to simulate unauthorized access attempts
usernames = ['admin', 'root', 'user1', 'guest']

# Define a list of event statuses
event_statuses = ['failed', 'success']

def generate_log_event(ip, user, status):
    # Get the current date and time
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Generate a log event
    log_event = f'{current_datetime} - Unauthorized access attempt by {ip} as {user} {status}'

    # Return the log event
    return log_event

# Open the log file in append mode
with open(log_file, 'a') as f:
    # Loop to generate multiple log events
    for _ in range(100):
        # Pick a random IP address, user name, and event status
        ip = random.choice(ip_addresses)
        user = random.choice(usernames)
        status = 'failed' if random.random() < 0.9 else 'success'  # 90% failure rate

        # Generate a log event
        log_event = generate_log_event(ip, user, status)

        # Write the log event to the log file
        f.write(log_event + '\n')

        # Sleep for a random amount of time between log entries
        time.sleep(random.uniform(0.1, 1.0))
        
        # End
        
        #GPT-4 was referenced for this code
