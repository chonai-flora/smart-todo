from django.core.management.base import BaseCommand
from django.utils import timezone
from smart_todo.models import *

import os
import environ
import requests
from pathlib import Path
from datetime import timedelta


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))


class Command(BaseCommand):
    help = '締切が近いtodosをLINEのトークルームにリマインドします'

    dbname = env('DATABASE_NAME')
    username = env('SUPERUSER_NAME')
    password = env('SUPERUSER_PASSWORD')
    line_token = env('LINE_TOKEN')

    # 締め切りの<days>日前のtodosを取得
    def generate_remind_message(self, days=1):
        upcoming_deadline_todos = Todo.objects.filter(
            deadline__gte=timezone.now(),
            deadline__lte=timezone.now() + timedelta(days=days)
        )

        messages = []
        for todo in upcoming_deadline_todos:
            if not todo.completed:
                messages.append((
                    f'\n「{todo.title}」の期限が近づいています。'
                    f'\n期限: {todo.deadline.strftime("%Y年%-m月%-d日")}'
                ))

        return '\n'.join(messages)

    def add_arguments(self, parser):
        parser.add_argument(
            '-d',
            dest='days',
            required=False,
            type=int,
            help='Remind todos to the LINE talk room <-d> days before the deadline.'
        )

    # LINE Notify APIを叩く
    def handle(self, *args, **options):
        days = options['days']
        message = self.generate_remind_message(days)

        endpoint = 'https://notify-api.line.me/api/notify'
        headers = { 'Authorization': 'Bearer ' + self.line_token }
        params = { 'message': message }
        response = requests.post(endpoint, headers=headers, data=params)
        http_status = response.status_code
        
        if http_status == 200:
            print('正常にトークルームに送信しました')
        else:
            print(f'トークルームに送信することができませんでした エラーコード: {http_status}')