import subprocess

def scan_wifi_networks():
    command = 'netsh wlan show networks mode=Bssid'
    result = subprocess.run(command, capture_output = True, text = True, shell = True)
    output = result.stdout
    return output

wifi_networks = scan_wifi_networks()
print(wifi_networks)