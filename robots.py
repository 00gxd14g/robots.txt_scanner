import urllib.request # veri çekme işlemi için urllib istek modülümüzü ekliyoruz.
import io

def get_robots_txt(url): # get_robots_txt adında oluşturduğumuz fonkisyona url parametresini ekliyoruz
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(req, encoding='utf-8') #request ardından okunacak response verisini utf8 e ceviriyoruz.
    return data.read()


print(get_robots_txt('https://wwww.reddit.com/'))
