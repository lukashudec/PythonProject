import requests
from xml.etree import ElementTree


def get_list_of_games():
    result = []
    response = requests.get('https://boardgamegeek.com//xmlapi2/hot?type=boardgame')
    print(response.status_code, response.text)
    tree = ElementTree.fromstring(response.content)
    for branch in tree:
        result.append([branch.attrib['rank'], branch.attrib['id'], branch[1].attrib['value']])
    return result
