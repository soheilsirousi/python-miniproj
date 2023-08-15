import subprocess

def crack_wifi_password(ssid):
    command = f'netsh wlan show profile name="{ssid}" key = clear'
    result = subprocess.run(command, capture_output = True, text = True, shell = True)
    output = result.stdout
    return output

def main():
    ssid = input('Enter the SSID of WiFi network: ')
    wifi_password = crack_wifi_password(ssid)
    print(wifi_password)

if __name__ == '__main__':
    main()