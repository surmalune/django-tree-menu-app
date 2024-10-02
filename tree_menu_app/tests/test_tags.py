from django.test import TestCase, RequestFactory
from django.template import Context
from django.template.base import Template
from tree_menu_app.models import MenuItem


class MenuTagTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = RequestFactory()

        cls.main_menu = MenuItem.objects.create(
            menu_name="main_menu", title="Main Menu", url="#")
        cls.sub_menu = MenuItem.objects.create(
            menu_name="main_menu", title="Sub Menu", parent=cls.main_menu, url="/sub-menu/")
        cls.sub_sub_menu = MenuItem.objects.create(
            menu_name="main_menu", title="Sub Sub Menu", parent=cls.sub_menu, url="/sub-menu/sub-sub-menu/")

    def test_draw_menu_with_active_item(self):
        request = self.factory.get('/sub-menu/')
        template = Template("{% load menu_tags %}{% draw_menu 'main_menu' %}")
        context = Context({'request': request})
        rendered = template.render(context)

        self.assertIn("Main Menu", rendered)
        self.assertIn("Sub Menu", rendered)
        self.assertIn("Sub Sub Menu", rendered)
        self.assertIn('class="active"', rendered)

    def test_draw_menu_without_active_item(self):
        request = self.factory.get('/')
        template = Template("{% load menu_tags %}{% draw_menu 'main_menu' %}")
        context = Context({'request': request})
        rendered = template.render(context)

        self.assertIn("Main Menu", rendered)
        self.assertNotIn("Sub Menu", rendered)
        self.assertNotIn("Sub Sub Menu", rendered)
        self.assertNotIn('class="active"', rendered)

    def test_draw_menu_with_active_nested_item(self):
        request = self.factory.get('/sub-menu/sub-sub-menu/')
        template = Template("{% load menu_tags %}{% draw_menu 'main_menu' %}")
        context = Context({'request': request})
        rendered = template.render(context)

        self.assertIn("Main Menu", rendered)
        self.assertIn("Sub Menu", rendered)
        self.assertIn("Sub Sub Menu", rendered)
        self.assertIn('class="active"', rendered)

    def test_draw_menu_with_nonexistent_menu(self):
        request = self.factory.get('/')
        template = Template(
            "{% load menu_tags %}{% draw_menu 'nonexistent_menu' %}")
        context = Context({'request': request})
        rendered = template.render(context)

        self.assertNotIn("Main Menu", rendered)
        self.assertNotIn("Sub Menu", rendered)
        self.assertNotIn("Sub Sub Menu", rendered)

    def test_empty_menu(self):
        request = self.factory.get('/')
        MenuItem.objects.all().delete()
        template = Template("{% load menu_tags %}{% draw_menu 'main_menu' %}")
        context = Context({'request': request})
        rendered = template.render(context)

        self.assertNotIn("Main Menu", rendered)
        self.assertNotIn("Sub Menu", rendered)
        self.assertNotIn("Sub Sub Menu", rendered)
