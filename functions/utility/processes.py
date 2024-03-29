import psutil

# Kill/terminate any open process with a spesific name <process_name, RobloxPlayerBeta.exe>
def terminate_process(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            proc.kill()
            print(f"Process {process_name} terminated.")
            return True
    print(f"No process named {process_name} found.")
    return False
