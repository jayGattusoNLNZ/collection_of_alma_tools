#### this is the agreed API key managamgent method. There are others, this is ours. 
#### Written by Sveltlana Koroteeva

"""This works by having a file called "secrets.txt" stored somewhere your machine can see. 
"secrets" contains your key in a way this script can find
We use this method so we can share alma scripts without exposing our personal keys

You can change the variable names to suit your usage, as long as you match secrets.txt with this part of your script.

Results in the var alma_bibskey being creatd that you can inculde in your API calls. 

This method can be extended to support as many keys as you need to managed.

For the reamaining examples in the tools set we will only use this method to manage API keys."""

import configparser

#enter the path to your secret file
secret_file=r"H:\secrets"

config = configparser.ConfigParser()
config.read(secret_file)

#uncomment the key you would like to use
## Make sure you're picking the right ALMA environment...

#alma_bibskey = config.get("configuration", "my_alma_prod_key") #PRODUCTION BIB (Bibliographic + Acquisition)
#alma_bibskey = config.get("configuration", "my_alma_sandbox_key")    #SB BIB (Bibliographic + Acquisition)

print(alma_bibskey)


"""
Example "secrets" file that would be used for the above implementation:
"""
[configuration]
my_alma_prod_ke = "aabbccddeeff"
my_alma_sandbox_key = "ffeeddccbbaa"
