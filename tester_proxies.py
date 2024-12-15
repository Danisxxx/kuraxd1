import requests
import time

def check_proxy(proxy):
    proxies = {"http": proxy}
    try:
        response = requests.get("http://www.google.com", proxies=proxies, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        return False

def clean_proxies():
    while True:
        with open("proxys.txt", "r") as file:
            proxies = file.readlines()
        
        cleaned_proxies = []
        
        for proxy in proxies:
            proxy = proxy.strip()  
            if check_proxy(proxy):
                cleaned_proxies.append(proxy)
                print(f"Proxy válido encontrado: {proxy}")
            else:
                print(f"Proxy no válido: {proxy}")
        
        # Guardar los proxies válidos en el archivo proxy.txt
        with open("proxys2.txt", "a") as file:
            file.write("\n".join(cleaned_proxies))
        
        time.sleep(60)  

if __name__ == "__main__":
    clean_proxies()
