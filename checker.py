import requests

# List of websites to monitor
websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org",
    "https://www.rancher.com" # A little nod to one of your target companies!
]

def run_check():
    print("--- Starting Website Status Check ---")
    for url in websites:
        try:
            response = requests.get(url, timeout=5)
            # 200 is the standard HTTP success code
            if response.status_code == 200:
                print(f"✅ SUCCESS: {url} is live!")
            else:
                print(f"⚠️ WARNING: {url} returned status {response.status_code}")
        except Exception as e:
            print(f"❌ ERROR: {url} could not be reached. {e}")
    print("--- Check Complete ---")

if __name__ == "__main__":
    run_check()