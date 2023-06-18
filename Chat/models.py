from django.db import models

from Auth.models import User


class ChatRoom(models.Model):
    """ Chat room model """
    title = models.CharField('Название комнаты', max_length=255)
    is_active = models.BooleanField('Комната активен', default=True)
    participants = models.ManyToManyField(User)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class ChatMessage(models.Model):
    """ Message of chat room """
    TYPE_MESSAGE = (
        ('text', 'Текст'),
        ('photo', 'Фото'),
        ('video', 'Видео'),
        ('audio', 'Звук'),
        ('voice', 'Голосовое'),
    )

    type_message = models.CharField(
        'Тип сообщения', choices=TYPE_MESSAGE, default='text', max_length=255)
    text_message = models.TextField(
        'Текст сообщения', max_length=4096, blank=True, null=True)
    file_message = models.FileField(
        'Файл сообщения', upload_to='files', blank=True, null=True)
    room = models.ForeignKey(
        ChatRoom, verbose_name='Комната сообщения', on_delete=models.CASCADE,
        related_name='room')
    sender = models.ForeignKey(
        User, verbose_name='Отправитель сообщения', on_delete=models.SET_NULL,
        related_name='sender', null=True)
    readers = models.ManyToManyField(User, verbose_name='Кто прочитал')

    def __str__(self):
        return f'{self.sender}, {self.type_message}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
