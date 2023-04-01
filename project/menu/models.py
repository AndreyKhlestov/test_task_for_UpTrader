from django.db import models


class MenuItemModel(models.Model):
    """Модель для древовидного меню"""
    title = models.CharField(max_length=50)

    # имя меню (для идентификации меню на странице)
    menu_name = models.CharField(max_length=50)

    slug = models.CharField(max_length=50, blank=True)
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
            
        # self.url = reverse('menu', args=[url_path])
        self.url = url_path
        super().save(*args, **kwargs)
