from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, UserViewSet, ManageUserView

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('myself/', ManageUserView.as_view(), name='myself'),
    path('', include(router.urls)),
]

'''
【解説】

このコードは、Django REST Framework（DRF）を使用したAPIのURLパスを設定しています。各行を初心者向けに分かりやすく説明していきます。

### インポート部分

1. `from django.urls import path`: Djangoの`path`関数をインポートします。この関数は、URLパターン（ウェブページのアドレスのパターン）をビュー（ウェブページのコンテンツを生成する関数やクラス）にマッピング（結び付け）する際に使用されます。
2. `from django.conf.urls import include`: `include`関数をインポートします。これは、別のURLconf（URL設定）モジュールを現在のURLconfに組み込むために使います。これにより、アプリケーションのURLパターンをモジュール化し、再利用性を高めることができます。
3. `from rest_framework import routers`: DRFの`routers`をインポートします。ルータは、ビューセット（APIの各エンドポイントを処理するビューの集合）に対するURLルーティングを自動的に処理します。
4. `from api.views import TaskViewSet, UserViewSet, ManageUserView`: `api/views.py`から、`TaskViewSet`, `UserViewSet`, `ManageUserView`をインポートします。これらは、APIのエンドポイントとして機能するビューです。

### ルータの設定

5. `router = routers.DefaultRouter()`: DRFのデフォルトルータをインスタンス化します。このルータは、ビューセットからURLパターンを自動的に生成します。
6. `router.register('tasks', TaskViewSet)`: `TaskViewSet`を`tasks`というURLパスでルータに登録します。これにより、`TaskViewSet`のアクション（例: リスト表示、詳細表示など）に対応するURLパターンが自動的に生成されます。
7. `router.register('users', UserViewSet)`: 同様に、`UserViewSet`を`users`というURLパスでルータに登録します。これにより、ユーザー関連のアクションに対応するURLパターンが生成されます。

### URLパターンの定義

8. `urlpatterns = [...]`: `urlpatterns`リスト内でURLパターンを定義します。このリストに含まれる各パターンは、特定のURLがリクエストされた際にどのビューを呼び出すかをDjangoに指示します。
9. `path('myself/', ManageUserView.as_view(), name='myself')`: `myself/`というURLパスで`ManageUserView`を呼び出します。`as_view()`はクラスベースビューを関数として呼び出せるようにするメソッドです。`name='myself'`はこのパターンに名前を付け、テンプレートやビューから参照しやすくします。
10. `path('', include(router.urls))`: ルータで生成されたすべてのURLパターンをルートURLパス（`''`）に組み込みます。これにより、`router`に登録されたビューセットのURLパターンがアプリケーションのURLパターンに含まれるようになります。

要約すると、このコードは`tasks`と`users`に対応するAPIエンドポイントのURLパターンを自動的に生成し、`myself/`パスで`ManageUserView`を直接指定するURLパターンを設定しています。これにより、DRFを用

いた効率的でシステマティックなAPIのルーティングが可能になります。
'''