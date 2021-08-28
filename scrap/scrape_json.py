import urllib.request
import json


def get_sum_of_count():
    url = input("Enter the API URL( skip it to use the defult ): ") or "http://py4e-data.dr-chuck.net/comments_1257064.json"
    response = urllib.request.urlopen(url)
    data = response.read().decode()
    js = json.loads(data)

    counts = 0
    for item in js['comments']:
        counts += item['count']
    return counts


count = get_sum_of_count()
print(count)