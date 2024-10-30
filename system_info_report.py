import os
import platform
import socket
import datetime
import psutil  # Requires installation of psutil library

def gather_system_info():
    system_info = {}

    # Basic system information
    system_info['System Name'] = platform.system()
    system_info['System Version'] = platform.version()
    system_info['Architecture'] = platform.architecture()[0]
    system_info['Machine Name'] = platform.node()
    system_info['User Name'] = os.getlogin()
    
    # Network information
    system_info['IP Address'] = socket.gethostbyname(socket.gethostname())

    # CPU information
    system_info['CPU Count'] = psutil.cpu_count(logical=True)
    system_info['CPU Frequency'] = f"{psutil.cpu_freq().current} MHz"

    # Memory information
    memory = psutil.virtual_memory()
    system_info['Total Memory'] = f"{memory.total / (1024 ** 3):.2f} GB"
    system_info['Available Memory'] = f"{memory.available / (1024 ** 3):.2f} GB"

    # Disk information
    disk = psutil.disk_usage('/')
    system_info['Total Disk Space'] = f"{disk.total / (1024 ** 3):.2f} GB"
    system_info['Used Disk Space'] = f"{disk.used / (1024 ** 3):.2f} GB"
    system_info['Free Disk Space'] = f"{disk.free / (1024 ** 3):.2f} GB"

    # Scan date and time
    system_info['Scan Date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return system_info

def write_report(info):
    # Set the report file path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    report_file_path = os.path.join(desktop_path, "system_report.txt")

    with open(report_file_path, 'w', encoding='utf-8') as f:
        for key, value in info.items():
            f.write(f"{key}: {value}\n")

    print(f"Report has been created at: {report_file_path}")

if __name__ == "__main__":
    system_info = gather_system_info()
    write_report(system_info)
