from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # 版本2x以上需要加上 on_delete=models.CASCADE

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    #
    def __str__(self):
        """返回模型的字符串表示"""
        # return self.text[:50] + "..."
        return self.text
    # def __str__(self):
    #     if len(self.text) > 50:        #设置当字数50以上时后面用省略号显示
    #         show_text = self.text[:50] + "..."
    #     else:
    #         show_text = self.text
    #     return show_text
