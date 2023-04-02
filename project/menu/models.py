from django.db import models


class MenuModel(models.Model):
    "Модель для древовидного меню"
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'


class MenuItemModel(models.Model):
    """Объекты модели для древовидного меню"""
    title = models.CharField(max_length=50)

    # имя меню (для идентификации меню на странице)
    menu_name = models.ForeignKey(
        MenuModel,
        null=True,
        on_delete=models.CASCADE,
        related_name='menu_item'
    )

    slug = models.CharField(max_length=50, blank=True, unique=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )
    url = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        url_path = self.slug
        parent = self.parent
        while parent is not None:
            url_path = parent.slug + '/' + url_path
            parent = parent.parent
        self.url = '/' + url_path + '/'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Menu Section'
