from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reset_token = models.CharField(max_length=100, default="")
    reset_token_expires = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    hashed_password = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name


class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'chat'

    def __str__(self):
        user_name = self.user.name if self.user else "No User"
        return f"{self.name} - {user_name}"


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    is_user_message = models.BooleanField(default=True)  # True for user, False for bot
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'message'

    def __str__(self):
        return f"{self.chat.name}: {self.content[:50]}..."
