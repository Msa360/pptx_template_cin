import requests

def check_sources_http(sources):
    for source in sources:
        r = requests.get(source)
        if r.status_code != 200:
            print(f"uncertainty with {source}, code: {r.status_code}")

if __name__ == "__main__":
    check_sources_http([])
