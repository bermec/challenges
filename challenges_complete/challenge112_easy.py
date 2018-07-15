'''
Wikipedia log-in URL is the following:

http://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page

Note how the URL has the Query String "?title=..", where the value "title" is
"Special:UserLogin" and "returnto" is "Main+Page"?

Your goal is to, given a website URL, validate if the URL is well-formed,
and if so, print a simple list of the key-value pairs! Note that URLs only
allow specific characters (listed here) and that a Query String must always
be of the form "<base-URL>[?key1=value1[&key2=value2[etc...]]]"

Formal Inputs & Outputs:

Input Description:

String GivenURL - A given URL that may or may not be well-formed.

Output Description:

If the given URl is invalid, simply print "The given URL is invalid".
If the given URL is valid, print all key-value pairs in the following format:

key1: "value1"
key2: "value2"
key3: "value3"
etc...

Sample Inputs & Outputs:

Given "http://en.wikipedia.org/w/index.php?title=Main_Page&action=edit",
your program should print the following:

title: "Main_Page"
action: "edit"

Given "http://en.wikipedia.org/w/index.php?title= hello world!&action=é",
your program should print the following:

The given URL is invalid

(To help, the last example is considered invalid because space-characters and
unicode characters are not valid URL characters)
'''
import re

url = 'http://worldofwater.com/index.php?cat=Blagdon_Minipond_Duo_Filter_Kits'
# cat, Blagdon....
url2 = 'http://flightscan.com/sites/adenairways.html'
# invalid
url3 = 'http://www.crazyguyonabike.com/doc/?o=1gci&doc_id=1885&v=f'
# o:lgc..., doc_id:1885, v:f
url4 = 'https://www.google.com/search?q=opening+curry%27s+leicester&ie=utf-8' \
       '&oe=utf-8&client=firefox-b&gfe_rd=cr&dcr=0&ei=Owu4Wb81p8fwB96FgbgC&np' \
       'sic=0&rflfq=1&rlha=0&rllag=52615959,-1148382,2989&tbm=lcl&rldimm=145' \
       '91543859091359834&ved=0ahUKEwi4svjKiKDWAhXSJFAKHfklCv0QvS4IQTAA&tbs=l' \
       'rf:!2m4!1e17!4m2!17m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:4#gfe_rd=cr&rlfi=h' \
       'd:;si:14591543859091359834;mv:!1m3!1d22306.60008864256!2d-1.1483827!3' \
       'd52.61595964999999!2m3!1f0!2f0!3f0!3m2!1i188!2i221!4f13.1;tbs:lrf:!2m1!' \
       '1e3!2m4!1e17!4m2!17m1!1e2!3sIAE,lf:1,lf_ui:4'

urls = [url, url2, url3, url4]

for url in urls:
    print(url)
    ans2 = re.findall('(\w+(?=\=))', url)
    ans3 = re.findall('\=([A-z\d\+\%]+|\d+)+', url)
    if ans2 == []:
        print('The given url is invalid.')
        print()
        continue
    for x in range(0, len(ans2)):
        print('{0}{1}{2}'.format(ans2[x], ': ', ans3[x]))
    print()