def remove_all_856_from_record(record, trigger_string)	
    """ you need to know what subfield you expect the trigger to be in, and sdjust line 5 accordingly"""
    my_856s = record.get_fields("856")
    for my_856 in my_856s:
      if trigger_string in my_856["u"]
				record.remove_field(my_856)    
     return record
