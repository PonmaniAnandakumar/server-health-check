
import psutil
import sys
from datetime import datetime

# ==============================
# Server Health Thresholds
# ==============================

CPU_WARNING = 70
CPU_CRITICAL = 90

MEM_WARNING = 70
MEM_CRITICAL = 90

DISK_WARNING = 80
DISK_CRITICAL = 95


# ==============================
# Function to determine status
# ==============================

def get_status(value, warning, critical):
    if value >= critical:
        return "CRITICAL"
    elif value >= warning:
        return "WARNING"
    else:
        return "HEALTHY"


# ==============================
# Main Health Check
# ==============================

def main():

    # Get system information
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    # Determine individual statuses
    cpu_status = get_status(
        cpu,
        CPU_WARNING,
        CPU_CRITICAL
    )

    memory_status = get_status(
        memory,
        MEM_WARNING,
        MEM_CRITICAL
    )

    disk_status = get_status(
        disk,
        DISK_WARNING,
        DISK_CRITICAL
    )

    # Determine overall server status
    statuses = [
        cpu_status,
        memory_status,
        disk_status
    ]

    if "CRITICAL" in statuses:
        overall = "CRITICAL"
    elif "WARNING" in statuses:
        overall = "WARNING"
    else:
        overall = "HEALTHY"

    # ==============================
    # Display Health Report
    # ==============================

    print("=" * 45)
    print("        SERVER HEALTH REPORT")
    print("=" * 45)

    print(f"Timestamp       : {datetime.now()}")
    print(f"CPU Usage       : {cpu}% [{cpu_status}]")
    print(f"Memory Usage    : {memory}% [{memory_status}]")
    print(f"Disk Usage      : {disk}% [{disk_status}]")

    print("-" * 45)
    print(f"Server Status   : {overall}")
    print("=" * 45)

    # ==============================
    # Jenkins Exit Codes
    # ==============================

    if overall == "CRITICAL":
        sys.exit(2)

    elif overall == "WARNING":
        sys.exit(1)

    else:
        sys.exit(0)


# ==============================
# Start Program
# ==============================

if __name__ == "__main__":
    main()

