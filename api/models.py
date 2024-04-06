from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)#登録時に自動で現在日時を追加
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title # アドミン画面でタスク一覧確認時に、どのタスクか識別子やすくするためにリターン