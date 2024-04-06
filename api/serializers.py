from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User # Djangoの組み込みユーザーモデル
from rest_framework.authtoken.models import Token # トークンは、APIを利用する際にユーザーを認証するために使用される

'''
Userモデルとシリアライザーを連携させるためのクラス
ModelSerializerはDRFが提供する機能で、モデルインスタンスをJSON形式に変換したり、JSONデータをモデルインスタンスに変換するためのロジックを自動的に提供します
'''
class UserSerializer(serializers.ModelSerializer):
    # モデルとフィールドの設定を行う
    class Meta:
        # Userモデルをシリアライザに関連付けます。これにより、Userモデルのデータを扱うことができる
        model = User

        # シリアライザを通して扱うUserモデルのフィールドを指定。ユーザーのID、ユーザーネーム、パスワードが含まれる
        fields = ['id', 'username', 'password']

        '''
        パスワードフィールドに追加の設定を施す。

        write_only: パスワードが書き込み専用であり、APIのレスポンスには含まれないことを意味する
        つまり、パスワードはシリアライザーを通してデータを受け取る際には設定できるが、シリアライズされたデータには含まれません。
        セキュリティを向上させるため

        required:パスワード必須のため
        '''
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # createメソッドをオーバーライド.検証済みデータから新しいUserインスタンスを作成する
    def create(self, validated_data):
        '''
        検証済みデータからユーザーを作成します。
        create_userはDjangoが提供するユーザー作成用のヘルパーメソッドで、パスワードを適切にハッシュ化します。
        ユーザーから受け取ったパスワードをハッシュ化してDBに保存するため。
        '''
        user = User.objects.create_user(**validated_data)
        #  新しく作成されたユーザーに対して認証トークンを生成し、データベースに保存します。
        Token.objects.create(user=user)
        # 新しく作成されたユーザーインスタンスを返す
        return user

# Taskモデルのデータをシリアライズ/デシリアライズするためのクラス
class TaskSerializer(serializers.ModelSerializer):
    '''
    created_atフィールドをシリアライズするためのフィールド定義。
    指定されたフォーマットで日時がシリアライズされ、read_only=Trueにより、このフィールドは読み取り専用に設定される
    '''
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        # Taskモデルをシリアライザに関連付け
        model = Task
        # シリアライザを通して扱うTaskモデルのフィールドを指定
        fields = ['id', 'title', 'created_at', 'updated_at']