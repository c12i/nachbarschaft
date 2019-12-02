from django.test import TestCase
from . import models
from neighborhood.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your tests here.

class TestPost(TestCase):

    def setUp(self):
        self.new_user = User(username="collins", email="test@test.com", password="qwerty123")
        self.new_user.save()
        self.new_group = models.Group(name="Test Community", location="City", 
                                      description="<p>None</p>\n", police_contact=911, hospital_contact=911)
        self.new_group.save()
        self.new_post = models.Post(user=self.new_user, message="<p>Hello</p>\n", 
                                    group=self.new_group)
        self.new_post.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, models.Post))

    def test_misaka(self):
        self.assertEqual(self.new_post.message_html, self.new_post.message)

    def test_save(self):
        self.new_post.save()
        posts = models.Post.objects.all()
        self.assertTrue(len(posts)>0)
        