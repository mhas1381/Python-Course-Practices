from bs4 import BeautifulSoup
with open('website.html' , encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents , 'html.parser')

# print(soup.title.string)
# print(soup.prettify())

all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.get_text())
#     print(tag.get('href'))

# heading = soup.find(name = 'h1' , id='name')
# print(heading)
#
# section_heading = soup.find(name = 'h3' , class_ = 'heading')
# print(section_heading.text)

company_url = soup.select_one(selector = "p a")
print(company_url)

headings = soup.select(".heading")
print(headings)