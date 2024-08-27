import datetime
import re
import string
import urllib.request
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

pattern = r"\d{5}"  # 5 digits regex

def get_url(subcode):
    return ("https://handbook.uts.edu.au/subjects/" + subcode + ".html")

# def soup_function():
sub_code = input("Enter sub code: ")
url = "https://handbook.uts.edu.au/subjects/" + sub_code + ".html"
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page, features="html.parser")

br_element = soup.find_all("br")[0]
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
print(thislist)

# get_url(31267)
# soup_function()
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