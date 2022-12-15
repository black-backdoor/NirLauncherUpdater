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

class config():
    def get_current_installed_version():
        old_versions = []
        with open("saves/version.txt") as file:
            for line in file:
                line = line.rstrip("\n")
                old_versions.append(line)
        return old_versions[0]

    def write_current_installed_version(version):
        myfile = open("saves/version.txt", "w+")
        myfile.write(new_version)
        myfile.close()

    def write_to_all_version(version):
        myfile = open("saves/versions.txt", "a")
        myfile.write("\n" + new_version)
        myfile.close()

    def config(file_path):
        with open(file_path, "r") as f:
            return json.load(f)

new_version = update_launcher.get_nirlauncher_version()


old_version = config.get_current_installed_version()
if not (old_version == new_version):
    print("new version online")
    print(new_version)
    config.write_current_installed_version(new_version)
    config.write_to_all_version(new_version)


#print(update_launcher.get_nirlauncher_link_downlad())