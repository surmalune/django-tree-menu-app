# Django Tree Menu App
This project implements a dynamic, tree-like menu system using Django Templates.

## Features
- Menu is manageable through Django admin
- Supports hierarchical menus with parent-child relationships
- Menu can be displayed dynamically on any page by its name
- Active menu item is highlighted based on the current URL
- Just one query per menu render, as verified by the Django Debug Toolbar:

```sql
SELECT "tree_menu_app_menuitem"."id", "tree_menu_app_menuitem"."menu_name", "tree_menu_app_menuitem"."title", "tree_menu_app_menuitem"."parent_id", "tree_menu_app_menuitem"."url", "tree_menu_app_menuitem"."named_url", "tree_menu_app_menuitem"."order"
FROM "tree_menu_app_menuitem"
WHERE "tree_menu_app_menuitem"."menu_name" = 'main_menu' 
ORDER BY "tree_menu_app_menuitem"."order" ASC;
```

## Installation
1. Clone the repository:
```bash
git clone https://github.com/surmalune/django-tree-menu-app.git
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Apply migrations:
```bash
python manage.py migrate
```
4. Create a superuser to access the admin panel:
```bash
python manage.py createsuperuser
```
5. Run the development server:
```bash
python manage.py runserver
```

## Usage
1. Add menu items in the Django admin. Ensure that the URLs you specify for each menu item are defined in your `urls.py` file.
2. Use the `draw_menu` template tag to render a menu by name:
```bashы
{% load menu_tags %}
{% draw_menu 'main_menu' %}
```

## Testing
To run tests, use the following command:
```bash
python manage.py test tree_menu_app.tests
```
