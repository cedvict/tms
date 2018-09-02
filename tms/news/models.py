from django.db import models


class News(models.Model):
    detail = models.CharField(max_length=100)
    created_date = models.DateTimeField('date created', auto_now_add=True, blank=True)
    upd_date = models.DateTimeField('date updated', auto_now=True, blank=True)

    def __str__(self):
        return self.detail

    class Meta:
        db_table = 'news_tab'
