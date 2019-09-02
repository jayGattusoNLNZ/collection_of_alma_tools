def add_856(record, link):
	"""takes a pymarc record and a permalink, adds the properly formatted permalink, returns record"""
	tag = '856'
	indicators = ["4","0"]
	subfields = ['u', link,
				 'z', "Archived copy available at the National Library of New Zealand", 
				 'x', "Open Access"]

	new_856 = Field(tag, indicators, subfields)
	record.add_ordered_field(new_856)
	return record
