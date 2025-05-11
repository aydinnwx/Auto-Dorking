
# auto_dorking.py
from googlesearch import search
import os
from pyfiglet import Figlet

def banner():
    f = Figlet(font='slant')
    print("\033[1;32m" + f.renderText("AutoDorking") + "\033[0m")
    print(" " * 10 + "\033[1;37mAuthor:\033[0m \033[1;36mm4lw4r2\033[0m\n")

def load_dorks(folder):
    dorks = {}
    for fname in ["filetype.txt", "intext.txt", "inurl.txt", "intitle.txt"]:
        path = os.path.join(folder, fname)
        if os.path.exists(path):
            with open(path, "r") as f:
                lines = [line.strip() for line in f if line.strip()]
                key = fname.split(".")[0]
                dorks[key] = lines
        else:
            print(f"[!] {fname} none.")
    return dorks

def dork_search(domain, dorks):
    for dork_type, values in dorks.items():
        print(f"\n[+] {dork_type}:")
        for value in values:
            query = f"site:{domain} {dork_type}:{value}" if dork_type == "filetype" else f"site:{domain} {dork_type}:{value}"
            print(f"[>] Searching: {query}")
            try:
                results = list(search(query, num_results=5))
                if results:
                    for url in results:
                        print(url)
                else:
                    print("[!] Not Found [-]")
            except Exception as e:
                print(f"[Error] {str(e)}")

if __name__ == "__main__":
    banner()
    domain = input("\n(without http/s) domain: ").strip()
    dork_folder = "/storage/emulated/0/Download" 
    dorks = load_dorks(dork_folder)
    dork_search(domain, dorks)