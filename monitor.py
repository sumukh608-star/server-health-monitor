import random

# --- CONFIG ---
SERVER_NAME = "Prod-Server-Alpha"
CPU_THRESHOLD = 90 
# --------------

def check_server():
    print(f"Checking {SERVER_NAME}...")
    cpu_usage = random.randint(1, 100)
    
    if cpu_usage > CPU_THRESHOLD:
        print(f"ALERT: High CPU Usage! {cpu_usage}%")
    else:
        print(f"System Normal: {cpu_usage}%")

check_server()