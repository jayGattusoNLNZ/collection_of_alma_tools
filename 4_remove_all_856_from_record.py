def remove_all_856_from_record(record)	
    my_856s = record.get_fields("856")
    for my_856 in my_856s:
				record.remove_field(my_856)    
     return record
