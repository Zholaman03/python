from django.db import models

class Sentences(models.Model):
    title = models.CharField('Название', max_length=250)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'{self.id}'
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

