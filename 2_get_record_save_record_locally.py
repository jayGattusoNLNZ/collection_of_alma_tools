
import requests
import configparser
from bs4 import BeautifulSoup as Soup

secret_file=r"H:\secrets"
config = configparser.ConfigParser()
config.read(secret_file)
alma_bibskey = config.get("configuration", "my_alma_sandbox_key")    #SB BIB (Bibliographic + Acquisition)


mms_id = 123123123123123
url = f"https://api-eu.hosted.exlibrisgroup.com/almaws/v1/bibs?view=full&expand=None&apikey={alma_bibskey}&mms_id={mms_id}"

### results in a BeautifulSoup item that can searched etc
my_record = Soup((requests.get( url, headers={'content-type': 'application/xml' }).text), 'lxml').find("bib")

print (my_record.find("datafield", tag="245").find("subfield", code="a").text, my_record.find("datafield", tag="245").find("subfield", code="b").text)
print (my_record.find("title").text)

### saves in the current dir as mms_id.xml, so in this case, 123123123123123.xml
### consider using  folders to help put files in useful locations e.g f"my_records/{mms_id}.xml"
with open(f"{mms_id}.xml", "wb", encoding="utf-8") as data:
	data.write(str(my_record)) 
