from django.db import models


class Item(models.Model):
    message = models.CharField(max_length=50, verbose_name='内容')
    done = models.BooleanField(default=False, verbose_name='是否完成')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = '事件'
        verbose_name_plural = '时间'
        ordering = ['-created_time']

    def toggle_done(self):
        self.done = bool(1-self.done)