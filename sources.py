import requests

def check_sources_http(sources):
    n = len(sources)
    errors = 0
    for i in range(n):
        try:
            r = requests.get(sources[i], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5640.226 Safari/537.36 Edg/111.0.1690.49', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'})
            if 200 < r.status_code < 400:
                print(f"uncertainty with {sources[i]}, code: {r.status_code}")
                errors += 1
            elif r.status_code >= 400: 
                print(f"Error with {sources[i]}, code: {r.status_code}")
                errors += 1
        except:
            print(f"Error with {sources[i]}")
            errors += 1
    if errors == 0: print("[+] success [+]")
    else: print(f"[-] {errors} failed [-]")


if __name__ == "__main__":
    check_sources_http([
        "https://explodingtopics.com/blog/corporate-cloud-data",
        "https://www.cengn.ca/services/commercialization-services/smart-agriculture-program/",
        "https://www.cloudflare.com/application-services/",
        "https://vercel.com/docs/concepts/edge-network/overview",
        "https://www.iothub.com.au/news/chevron-scales-up-industrial-iot-pilot-513758",
        "https://www.datacenterknowledge.com/microsoft/how-microsoft-extending-its-cloud-chevron-s-oil-fields",
        "https://www.lepoint.fr/services/menta-le-leader-europeen-de-la-reprogrammation-hardware-embarquee-28-03-2022-2469874_4345.php",
        "https://ori.co/multicloud-networking",
        "https://zededa.com/products/",
        "https://www.stengg.com/en/digital-tech/data-science-analytics-and-ai/video-analytics/",
        "https://www.stengg.com/en/digital-tech/data-science-analytics-and-ai/edge-analytics/"
    ])