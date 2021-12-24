import urllib.request

# Function to download url data
def download(URL):
    # Imitating firefox
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
    # Scraping html page for new link
    request = urllib.request.Request(URL, headers = headers)
    return urllib.request.urlopen(request)