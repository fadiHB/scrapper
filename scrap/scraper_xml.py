import xml.etree.ElementTree as ET
import urllib.request

def create_xmlFile_fromUrl(url, path):
    response = urllib.request.urlopen(url)
    xml = response.read().strip().decode()
    with open(path ,'w') as file:
        file.write(xml)

def parse_xml_from_url(url):
    response = urllib.request.urlopen(url)
    xml = response.read().strip().decode()

    # reading directly from a string:
    tree = ET.fromstring(xml)
    return tree


def parse_xml_from_file(url, path):
    create_xmlFile_fromUrl(url, path)

    # reading from a file:
    tree = ET.parse('./assets/xmlfile.xml')
    return tree

url = 'http://py4e-data.dr-chuck.net/comments_1257063.xml'
path = './assets/xmlfile.xml'


if __name__ == "__main__":
    tree = parse_xml_from_file(url, path)

    root = tree.getroot()
    print("root.tag:", root.tag)

    countsEl_list = tree.findall('comments/comment/count')
    sum_counts = 0
    for count in countsEl_list:
        sum_counts += int(count.text)

    print(sum_counts)
