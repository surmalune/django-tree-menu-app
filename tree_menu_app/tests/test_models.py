from django.test import TestCase
from tree_menu_app.models import MenuItem


class MenuItemModelTest(TestCase):
    def setUp(self):
        self.parent_item = MenuItem.objects.create(
            menu_name="main_menu", title="Home", url="/home/")
        self.child_item = MenuItem.objects.create(
            menu_name="main_menu", title="About Us", parent=self.parent_item, url="/about/")

    def test_get_url(self):
        self.assertEqual(self.parent_item.get_url(), "/home/")
        self.assertEqual(self.child_item.get_url(), "/about/")
