from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Book, Review

# Create your tests here.

class BookTests(TestCase): 
    def setUp(self): 
        self.book = Book.objects.create(
            title = "testBook", 
            author = "testAuthor", 
            price = '10.00'
        )
        self.user = get_user_model().objects.create_user( # new
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123'
        )
        self.review = Review.objects.create(book = self.book, author = self.user, review = "not bad")

    def test_book_listing(self): 
        self.assertEqual(f"{self.book.title}","testBook" )
        self.assertEqual(f"{self.book.author}","testAuthor" )
        self.assertEqual(f"{self.book.price}","10.00" )

    def test_book_list_view(self): 
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'testBook')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "not bad")
        self.assertTemplateUsed('books/book_detail.html')