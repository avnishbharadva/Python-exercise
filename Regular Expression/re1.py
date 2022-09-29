import re

# str = re.search("am","hello i am avnish am")

# str = re.search("^hello","hello i am avnish am")  # ^ = start with hello

# str = re.search("am$","hello i am avnish am") # $ = ends with am

# str = re.search("^hello.*am$","hello i am avnish am") # ^ = start with hello , . = vache gme e except new line char , * = zero or more occurrence , $ = ends with am

# str = re.search("[a-m]","hello i am avnish am") # [a-m] = search lower case character alphabetically between "a" and "m"

# str = re.search("he..o","hello i am avnish 69 am") # .. = Search for a sequence that starts with "he", followed by two (any) characters, and an "o"

# str = re.search("av.*h","hello i am avh 80 am") # * =  Search for a sequence that starts with "av", followed by 0 or more  (any) characters, and an "h" ( Zero or more occurrences )

# str = re.search("av.+h","hello i am avsh 80 am") # + =  Search for a sequence that starts with "av", followed by 1 or more  (any) characters, and an "h" ( One or more occurrences )

# str = re.search("av.?h","hello i am avsh 80 am") # ? =  Search for a sequence that starts with "av", followed by 0 or 1 (any) characters, and an "h" ( Zero or One occurrences )

# str = re.search("av.{2}h","hello i am avnsh 80 am") # {} =  Search for a sequence that starts with "av", followed excactly 2 (any) characters, and an "h"

# str = re.search("krishna|avnish","hello i am krishna am") # | = Check if the string contains either "krishna" or "avnish"

# str = re.search("\Ahey","hey avnish hehe") # \A = Check if the string starts with "hey"

# str = re.search("\d","acain sain 123 in Spain ain") # \d = Check if the string contains any digits (numbers from 0-9)

# str = re.search("\D","acain sain 123 in Spain ain") # \D = Return a match at every no-digit character

# str = re.search("\s","acain sain 123 in Spain ain") # \s = Return a match at every white-space character

# str = re.search("\s","acain sain 123 in Spain ain") # \S = Return a match at every NON white-space character

# str = re.search("\w","hey avnish hehe") # \w = Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character)

# str = re.search("\W","he!y avnish hehe") # \W = Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.)

str = re.search("he\Z","he!y avnish hehe") # \Z = Check if the string ends with "he"

if str==None:
    print("Not Found")
else:
    print("Found")
    print(str)
    print(str.group(0))
    print(str.span(0))
    print(str.span(0)[0],str.span(0)[1])