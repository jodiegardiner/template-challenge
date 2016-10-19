from pages import page_content

template = open('template.html', 'r')
content = template.read()
template.close()

i=0
for page in page_content:
    title = content.replace("{title}", page_content[page]['title'])
    heading = title.replace("{heading}", page_content[page]['heading'])
    body = heading.replace("{body}", page_content[page]['body'])
    url = page_content.keys()[i]
    i+=1
    new_page = open(url, 'w')
    new_page.write(body)
    new_page.close()

