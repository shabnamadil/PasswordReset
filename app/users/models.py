from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    full_name = models.CharField('İstifadəçinin adı, soyadı', max_length=100)
    phone_number = models.CharField('İstifadəçinin əlaqə nömrəsi', max_length=20, unique=True)
    email = models.EmailField('İstifadəçinin email ünvanı', unique=True)
    password = models.CharField('İstifadəçinin parolu', max_length=100)
    created_at = models.DateTimeField('İstifadəçinin yaradılma tarixi', auto_now_add=True, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'phone_number']
    username = None

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    class Meta:
        verbose_name = ('İstifadəçi')
        verbose_name_plural = ('İstifadəçilər')

    def __str__(self) -> str:
        return self.full_name
