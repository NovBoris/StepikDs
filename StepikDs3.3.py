# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">,
# возможно с дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C,
# что из A в C можно перейти за один переход и из C в B можно перейти за один переход.
#
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
#
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

# import requests
# import re
#
# result = False
#
# link1 = input()
# res1 = requests.get(link1)
# if res1.status_code == 200:
#     link2 = input()
#     for link in re.findall(r"<a href=\"(.*)\"", res1.text):
#         res = requests.get(link)
#         if res.status_code == 200:
#             for url in re.findall(r"<a href=\"(.*)\"", res.text):
#                 if link2 == url:
#                     result = True
#                     break
#             if result:
#                 break
# else:
#     result = False
#
# if result:
#     print("Yes")
# else:
#     print("No")

# второй вариант

# import re
# import requests
#
# start_url = input()
# end_url = input()
#
# found = False
#
# link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')
#
# resp = requests.get(start_url).text
#
# for url in link_pattern.findall(resp):
#     cur_resp = requests.get(url).text
#     if end_url in link_pattern.findall(cur_resp):
#         found = True
#         break
#
# print("Yes" if found else "No")
#
# Вашей программе на вход подается ссылка на HTML файл.
# Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... >
# и вывести список сайтов, на которые есть ссылка.
#
# Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть,
# это последовательность символов, которая следует сразу после символов протокола, если он есть,
# до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
# <a href="../some_path/index.html">.

# Сайты следует выводить в алфавитном порядке.

# import re
# import requests
#
# resp = requests.get(input()).text
# sites = set()
# for site in re.findall(r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)', resp):
#     sites.add(site)
#
# for site in sorted(sites):
#     print(site)
#
# # второй вариант
#
# import urllib.parse as urllib
# import requests
# from lxml import html
#
# url = input().rstrip()
# page = requests.get(url)
# tree = html.fromstring(page.text)
# hrefs = tree.xpath('//a/@href')
# url_set = set()
# for link in hrefs:
#     line = urllib.urlsplit(link)[1] if urllib.urlsplit(link)[1] else urllib.urlsplit(link)[2]
#     if line[0].isalpha():
#         url_set.add(line.split(':')[0]) if len(line.split(':')) > 1 else url_set.add(line)
# [print(x) for x in sorted(url_set)]
#
# # третий вариант
#
# from html.parser import HTMLParser
# import requests
# import urllib.parse
#
#
# class MyParser(HTMLParser):
#     links = set()
#
#     def handle_starttag(self, tag, attrs):
#         if tag == 'a':
#             for tpl in attrs:
#                 _url = urllib.parse.urlparse(tpl[1])
#
#                 if _url[1] and _url[1][-1].isalpha():
#                     self.links.add(_url[1])
#
#     def print(self):
#         return self.links
#
#
# request = requests.get(input()).text
# parser = MyParser()
# parser.feed(request)
#
# for item in sorted(parser.print()):
#     print(item)
