from django.test import TestCase
from account import models as amod
from django.contrib.auth.models import Permission, Group, ContentType

class UserModelTest(TestCase):

    fixtures = ['data.yaml']

    def setUp(self):
        self.u3 = amod.User.objects.get(email='Lisa@Simpsons.com')


    def test_user_create_save_load(self):
        '''Tests round trip of User model data to/from database'''
        u2 = amod.User.objects.get(email='Lisa@Simpsons.com')
        self.assertEquals(self.u3.first_name, u2.first_name)
        self.assertEquals(self.u3.last_name, u2.last_name)
        self.assertEquals(self.u3.email, u2.email)
        self.assertEquals(self.u3.password, u2.password)
        self.assertTrue(u2.check_password('Doh!'))

    def test_add_groups_check_permissions(self):
        '''Add groups to a user and check permissions'''
        # for p in Permission.objects.all():
        #     print(p.content_type.app_label + '.' + p.codename)
        p1 = Permission()
        p1.name = 'Change product price'
        p1.codename = 'change_product_price'
        p1.content_type = ContentType.objects.get(id=1)
        p1.save()

        g1 = Group()
        g1.name = 'Salespeople'
        g1.save()
        g1.permissions.add(p1)
        g1.save()
        self.u3.groups.add(g1)

        self.assertTrue(self.u3.has_perm('admin.change_product_price'))

    def test_add_and_test_permissions(self):
        p1 = Permission()
        p1.name = 'Change product price'
        p1.codename = 'change_product_price'
        p1.content_type = ContentType.objects.get(id=101)
        p1.save()
        self.u3.user_permissions.add(p1)

        self.assertTrue(self.u3.has_perm('account.change_product_price'))

    def test_password(self):
        '''Test the password'''
        self.u3.set_password('test_password')
        self.u3.save()
        u2 = amod.User.objects.get(email='Lisa@Simpsons.com')
        self.assertTrue(u2.check_password('test_password'))

    def test_change_fields(self):
        name = 'Bart'
        self.u3.first_name = name
        email = 'bart@simpsons.com'
        self.u3.email = email
        passw = 'DopeSauce'
        self.u3.set_password(passw)

        self.assertEquals(self.u3.first_name, name)
        self.assertEquals(self.u3.email, email)
        self.assertTrue(self.u3.check_password(passw))
