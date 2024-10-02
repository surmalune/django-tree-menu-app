from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class MenuItem(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children',
                               on_delete=models.CASCADE, verbose_name=_("Parent"))
    url = models.CharField(max_length=200, blank=True,
                           null=True, verbose_name=_("URL"))
    named_url = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Named URL"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Order"))
    menu_name = models.CharField(max_length=255, verbose_name=_("Menu Name"))
    
    class Meta:
        verbose_name = _("Menu Item")
        verbose_name_plural = _("Menu Items")
        ordering = ['order']

    def get_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url or '#'

    def __repr__(self):
        parent_title = self.parent.title if self.parent else "None"
        return f"<MenuItem(id={self.id}, menu_name={self.menu_name!r}, title={self.title!r}, parent={parent_title!r}, order={self.order})>"

    def __str__(self):
        return self.title