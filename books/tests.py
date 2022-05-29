import pytest
import requests

def test_import():

    url = 'https://www.googleapis.com/books/v1/volumes?q=author:'
    author = 'null'
    url_au = url+author
    response = requests.get(url_au)
    response = response.json()
    data = []
    print(' ----- imported: ', len(response['items']))
    print(' ----- type: ', type(response['items']))
    for item in response['items']:
        d = {}
        d['external_id'] = item['id']
        d['title'] = item['volumeInfo']['title']
        d['authors'] = item['volumeInfo']['authors']
        print('date: ', item['volumeInfo']['publishedDate'][0:4], type(item['volumeInfo']['publishedDate']))
        d['published_year'] = item['volumeInfo']['publishedDate']
        for k,v in item['volumeInfo'].items():
            if k == 'imageLinks':
                d['thumbnail'] = v['thumbnail']
                data.append(d)
    print(' - data: ', data)
