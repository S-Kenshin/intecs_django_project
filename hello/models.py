from django.db import models

#djangoはSQLへテーブルを記載するとき、以下のようにクラスを作る形でテーブルを作成する。
#変数がDBにおけるカラム名となる。
class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()
    
    #インスタンスを表示する(表示方法は自分で設定している)
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ',' + \
            self.name + '(' + str(self.age) + ')>'