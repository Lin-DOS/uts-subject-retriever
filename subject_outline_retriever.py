import datetime
import re
import string
import urllib.request
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

# url = input()

def get_url(subcode):
    return ("https://handbook.uts.edu.au/subjects/" + subcode + ".html")

def soup_function():
    subcode = input("Enter sub code: ")
    url = get_url(subcode)
    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page, features="html.parser")
    return soup

pattern = r"\d{5}"  # 5 digits regex

# element_string = tags.get_text(" ", strip=True)
def new_function():
    br_element = soup_function().find_all("br")[0]
    for tags in br_element.find_all_next("em", limit=3):
        element_string = tags.get_text()
        if "Requisite(s)" in element_string:
            requisites = element_string
            # print(requisites)
        if "Anti-requisite(s)" in element_string:
            antirequisites = element_string

        number = re.findall(pattern, requisites)
        thislist = []
        for j in number:
            url = get_url(j)
            thislist.append(url)
        print(thislist[4])
        return requisites
# get_url(31267)
print(new_function())
# find_requisites(thislist[4])
# label = soup.find_all("br")[0]
# labels = label.next_sibling
# # print(labels)
# for text in labels.stripped_strings:
#     print(text)
#

# n = datetime.datetime.now().year
# subjectCode = input("Enter subject code: ")
# subjectYear = input("Enter year: ")
# urllib.request.urlretrieve("https://cis-admin-api.uts.edu.au/subject-outlines/index.cfm/PDFs?lastGenerated=true&lastGenerated=true&subjectCode=" + subjectCode + "&year=" + subjectYear + "&session=SPR&mode=standard&location=city", filename="sub.pdf")
# print("Successfully downloaded subject outline for subject " + subjectCode + ", " + str(subjectYear))