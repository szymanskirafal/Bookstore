from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

import requests

from books.views import ApiSpecAPIView
from books.models import Book


class ApiSpecAPIViewTests(APITestCase):
    def test_get(self):
        url = reverse("api-spec")
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {"info": {"version": "2022.05.16"}}


class BooksViewSetTests(APITestCase):
    def test_get_list(self):
        url = reverse("book-list")
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_create(self):
        url = reverse("book-list")
        data = {"title": "Great Adventure", "authors": ["Johny"], 'published_year':2000,}
        response = self.client.post(url, data=data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == 'Great Adventure'
        assert response.data['authors'] == ['Johny']
        assert response.data['published_year'] == 2000


class ImportCreateAPIViewTests(APITestCase):

    def test_import(self):
        url = reverse("import")
        data={'authors': ["Brown"]}
        response = self.client.post(url, data=data, format="json")
        assert response.data == {'imported':10}
        assert response.status_code == status.HTTP_201_CREATED

    def test_import_create(self):
        url = reverse("import")
        data={'authors': "['Brown']"}
        response = self.client.post(url, data=data, format="json")
        #print(' resp: ', response.query_params)
        books = Book.objects.all()
        #.filter(authors=['Brown']).exists()
        for book in books:
            print('book: ', book)

    def test_req(self):
        url = 'https://www.googleapis.com/books/v1/volumes?q=author:'
        author = 'Diana'
        url_au = url+author
        response = requests.get(url_au)
        response = response.json()
        data = []
        print(' ----- url: ', url_au)
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
