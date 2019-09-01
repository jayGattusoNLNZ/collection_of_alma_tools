import requests
import configparser
from bs4 import BeautifulSoup as Soup

secret_file=r"H:\secrets"
config = configparser.ConfigParser()
config.read(secret_file)
alma_bibskey = config.get("configuration", "my_alma_sandbox_key")    #SB BIB (Bibliographic + Acquisition)

### need a list of valid mms ids for your ALMA instance
### can be int, can be str, they are turned into str later on for the url call 

my_list_of_mms_ids = [123123123123123, "123123123123124"]

for mms_id in my_list_of_mms_ids:

	url = f"https://api-eu.hosted.exlibrisgroup.com/almaws/v1/bibs?view=full&expand=None&apikey={alma_bibskey}&mms_id={my_mms}"

	### results in a BeautifulSoup item that can searched etc
	my_record = Soup((requests.get( url, headers={'content-type': 'application/xml' }).text), 'lxml').find("bib")


	### example usage as bs item
	print (my_record.find("datafield", tag="245").find("subfield", code="a").text, my_record.find("datafield", tag="245").find("subfield", code="b").text)
	print (my_record.find("title").text)

	### to work on the record as a string
	my_record_as_an_xml_string = str(my_record)
