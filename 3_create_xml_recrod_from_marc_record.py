    
from lxml import etree as et
from pymarc import MARCReader, record_to_xml

def convert_mrc_recorc_to_xml(my_marc):
	root = et.Element("collection")
	xml_record = record_to_xml(record)
	root.insert(i, et.fromstring(xml_record))
  return et.tostring(root, pretty_print=True).decode()
