from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    url = models.CharField(max_length=100, verbose_name='URL', help_text='Может быть пустым, если используется named URL')
    named_url = models.CharField(max_length=100, blank=True, null=True, verbose_name='Именованный URL')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    menu_name = models.CharField(max_length=50, verbose_name='Имя меню')
    is_active = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'