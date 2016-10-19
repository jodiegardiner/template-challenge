template = open('template.html', 'r')
content = template.read()
template.close()

title = content.replace("{title}", "Cool Page Title")
heading = title.replace("{heading}", "Cool Heading")
body = heading.replace("{body}", "What a cool Body this is")

title = content.replace("{title}", index['title'])
heading = title.replace("{heading}", index['heading'])
body = heading.replace("{body}", index['body'])
url = page_content[page]

new_page = open('index.html', 'w')
new_page.write(body)
new_page.close()

for page in page_content:
    print page_content[page]

    title = content.replace("{title}", page_content[page]['title'])
    heading = title.replace("{heading}", page_content[page]['heading'])
    body = heading.replace("{body}", page_content[page]['body'])
    url = page_content.keys()[0]
    print url

    new_page = open(url, 'w')
    new_page.write(body)
    new_page.close()
