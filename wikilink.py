import requests
from bs4 import BeautifulSoup

firstlink = input('first wikilink\n')
firstlink = "https://en.wikipedia.org/wiki/NASA"
secondlink = input('second wikilink\n')
secondlink = "https://en.wikipedia.org/wiki/Capital_city"

# response1 = requests.get(firstlink)

# soup1 = BeautifulSoup(response1.text, 'lxml')

def findlink(firstlink, targetlink, num, path):
    print("pathlength" + str(num) + " = " + str(path))
    if num > 10:
        print("no path found")
        return []
    print(firstlink+" there")
    if firstlink+'&' in path:
        print("loop found")
        return []
    firstlink = "https://en.wikipedia.org/w/api.php?action=parse&page=" + firstlink[30:len(firstlink)] + "&format=json"
    print(firstlink)
    response = requests.get(firstlink)
    soup = BeautifulSoup(response.text, 'lxml')
    links = soup.find_all('a')
    for link in links:
        s = link.get('href')
        if s and s[0:8] == "\\\"/wiki/" and s[8:13] != "File:":
            full_url = "https://en.wikipedia.org/wiki/"+s[8:len(s)-2]
            if full_url == targetlink:
                print('end state reached\n')
                print(path + [full_url])
                return path + [full_url]
            else:
                full_url
                result = findlink("https://en.wikipedia.org/wiki/"+s[8:len(s)-2], targetlink, num + 1, path + ["https://en.wikipedia.org/wiki/"+str(firstlink[53:len(firstlink)-11])])
                if result != []:
                    return result
        else:
            print("not a link")

            continue
path = findlink(firstlink, secondlink, 0, [])

# links1 = soup1.find_all('a')
# for link in links1:
#     s = str(link.get('href'))
#     print(s[0:8])
#     print(s[8:len(s)-2])
#     print(link.get('href'))


# description = soup.find('li', class_='post-732 product type-product status-publish has-post-thumbnail product_cat-flame product_cat-pokemon product_tag-blaze product_tag-charmeleon product_tag-flame first instock taxable shipping-taxable purchasable product-type-simple').text
# print(description)

# products = soup.find('ul', class_='products columns-4')
