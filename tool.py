
import requests

API_KEY = "9c557e2783f35db78aeb1bd2d753a4161b9bb6f0a756007c10ec3a7b4f2fb91e"

def load_wordlist(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def serpapi_search(query):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "api_key": API_KEY
    }
    response = requests.get(url, params=params)
    results = []
    if response.status_code == 200:
        data = response.json()
        for r in data.get("organic_results", []):
            link = r.get("link")
            if link:
                results.append(link)
    return results

def run_searches(site):
    print(f"\n[+] Axtarış başlayır: {site}\n")

    filetypes = load_wordlist("/storage/emulated/0/Download/filetype.txt")
    for ft in filetypes:
        query = f"site:{site} filetype:{ft}"
        print(f"\n[filetype:{ft}]")
        results = serpapi_search(query)
        if results:
            for r in results:
                print(r)
        else:
            print("[-] Heç nə tapılmadı")

    titles = load_wordlist("/storage/emulated/0/Download/intitle.txt")
    for title in titles:
        query = f"site:{site} intitle:{title}"
        print(f"\n[intitle:{title}]")
        results = serpapi_search(query)
        if results:
            for r in results:
                print(r)
        else:
            print("[-] Heç nə tapılmadı")

    urls = load_wordlist("/storage/emulated/0/Download/inurl.txt")
    for u in urls:
        query = f"site:{site} inurl:{u}"
        print(f"\n[inurl:{u}]")
        results = serpapi_search(query)
        if results:
            for r in results:
                print(r)
        else:
            print("[-] Heç nə tapılmadı")

    texts = load_wordlist("/storage/emulated/0/Download/intext.txt")
    for t in texts:
        query = f"site:{site} intext:{t}"
        print(f"\n[intext:{t}]")
        results = serpapi_search(query)
        if results:
            for r in results:
                print(r)
        else:
            print("[-] Heç nə tapılmadı")

if __name__ == "__main__":
    site = input("site: ").strip()
    run_searches(site)
