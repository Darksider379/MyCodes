import json
from difflib import SequenceMatcher######Python standard library to find best match from a string(longest continuous match)
from difflib import get_close_matches ########Python method to find the closest matching word
data=json.load(open(r'C:\Users\CHANDRABRATA\Desktop\Python Basic\UdemyResources\data.json')) #####loading json file into a dictionary object


def my_thesaurus(mykey):
    casefold=mykey.casefold() #########changing the case of key into smaller case
    closest_match=get_close_matches(casefold,data.keys(),cutoff=0.8)
    if casefold in data: ############Checking the key in data.json dictionary
        return data[casefold]
        
    elif len(closest_match) > 0 :
        choice=input("Did you mean {} (Y/N)? ".format(get_close_matches(casefold,data.keys(),cutoff=0.8)[0]))
        if choice in ['Y','y','N','n']:
            return data[get_close_matches(casefold,data.keys(),cutoff=0.8)[0]]
        else:
            return "Your did not enter the correct choice..Exiting the program. "


    else:
        return "The word doesn't exist.. Please check the word again"

        
choice=input('Enter your word: ')
print('You have chosen %s' %choice)
output=my_thesaurus(choice)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)



    