from bs4 import BeautifulSoup
url = 'https://www.bayt.com/en/jordan/jobs/python-developer-jobs/'
url2 = 'http://py4e-data.dr-chuck.net/comments_1257061.html'

# Get the HTML Page
### using urllib.request library
import urllib.request
response_1 = urllib.request.urlopen(url2)

status_code_1 = response_1.status
print("status code:", status_code_1)

html_text_1 = response_1.read().strip().decode()

with open('file_urllib.html', 'w') as file:
    file.write(html_text_1)



### using requests library
import requests
response_2 = requests.get(url)

status_code_2 = response_2.status_code
print("status code:", status_code_2)

html_text_2 = response_2.text
with open('file_request.html', 'w') as file:
    file.write(html_text_2)



# Parsing the HTML page using BeautifulSoup
soup = BeautifulSoup(html_text_1, 'html.parser')
spans = soup.find_all('span')
contents = [int(content.get_text()) for content in spans] 
print(sum(contents))

###################################################


url3 = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url4 = 'http://py4e-data.dr-chuck.net/known_by_Haneen.html'

#Retrive all of the anchor tags
def find_name(url):
    count = int(input('Enter count:'))
    pos = int(input('Enter position:'))
    for _ in range(count):
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html,'html.parser')
        all_tags = soup.find_all('a')
        target_tag = all_tags[pos-1]
        url = target_tag.get('href',None)

    # print(url)

    import re
    pattern = r"\_(.*?)\."
    name = re.findall(pattern, url)[0][3:]
    return name

print(find_name(url4))

if __name__ == "__main__":
    pass