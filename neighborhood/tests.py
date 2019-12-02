from django.test import TestCase
from . import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your tests here.
class TestGroup(TestCase):

    def setUp(self):
        self.new_group = models.Group(name="Test Community", location="City", 
                                      description="<p>None</p>\n", police_contact=911, hospital_contact=911)
        self.new_group.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_group, models.Group))

    def test_misaka(self):
        self.assertEqual(self.new_group.description_html, self.new_group.description)

    def test_slug(self):
        self.assertEqual(self.new_group.slug, "test-community")

    def test_save(self):
        self.new_group.save()
        groups = models.Group.objects.all()
        self.assertTrue(len(groups)>0)


class GroupMemberTest(TestCase):

    def setUp(self):
        self.new_user = User(username="collins", email="test@test.com", password="qwerty123")
        self.new_user.save()
        self.new_group = models.Group(name="Test Community", location="City", 
                                      description="<p>None</p>\n", police_contact=911, hospital_contact=911)
        self.new_group.save()

        self.new_member = models.GroupMember(user=self.new_user, group=self.new_group)
        self.new_member.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_member, models.GroupMember))


class BusinessTest(TestCase):
    def setUp(self):
        self.new_group = models.Group(name="Test Community", location="City", 
                                      description="<p>None</p>\n", police_contact=911, hospital_contact=911)
        self.new_group.save()
        self.new_business = models.Business(group=self.new_group, name="Testing",
                                            description="Lorem ipsum dolor", category="None")
        self.new_business.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business, models.Business))

    def test_create_business(self):
        self.new_business.save()
        businesses = models.Business.objects.all()
        self.assertTrue(len(businesses)>0)

    def test_find_business(self):
        self.new_business.save()
        business = models.Business.find_business(self.new_business.id)
        self.assertEqual(business[0], self.new_business)

    def search_businesses(self):
        self.new_business.save()
        business = models.Business.search_businesses("None")
        self.assertTrue(self.new_business in business)
