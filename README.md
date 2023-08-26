# smart-todo

## backend
### 1. `.env` を作成
```bash
cd backend/
cp .env.example .env
```

### 2. 環境変数を設定
以下の環境変数を設定する。
```makefile
DATABASE_NAME=""
SUPERUSER_NAME=""
SUPERUSER_PASSWORD=""
LINE_TOKEN=""
```

### 3. 実行
```bash
# 仮想環境をアクティベート
python3 -m venv .venv
source venv/bin/activate

# 必要なパッケージをインストール
pip3 install -r requirements.txt

# データベースのマイグレーションを実行
python3 manage.py migrate

# サーバーを起動
python3 manage.py runserver
```

### 余談: 締切が近いtodosをLINEのトークルームにリマインド
```bash
python3 manage.py remind -d <days>
```
`-d <days>`は省略可能(デフォルトで締切1日前までのtodosを取得)