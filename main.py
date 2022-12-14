import requests
from bs4 import BeautifulSoup
import json


url = "https://launcher.nirsoft.net/downloads/index.html"
class update_launcher():
    def get_nirlauncher_version():
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        version = str(soup)
        old, version = version.split('<td nowrap="">Current Package Version:\n<td>', 1)
        version, old = version.split('<tr>', 1)
        version = version.replace("\n", "")
        return version

    def get_nirlauncher_link_downlad():
        reqs = requests.get(url)
        download_link = str(reqs.text)
        old, download_link = download_link.split('<p>\n<a href="', 1)
        download_link, old = download_link.split('"><img src="download1.png" border="0"></a>', 1)
        download_link = "https:" + download_link
        return download_link

    def get_nirlauncher_downlad_zip(download_link):
        pass

class get_config():
    def config(file_path):
        with open(file_path, "r") as f:
            return json.load(f)

print(update_launcher.get_nirlauncher_version())
print(update_launcher.get_nirlauncher_link_downlad())