from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core import validators

from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class AccountManager(BaseUserManager):
    def _create_user(self, email, username, password, is_staff, is_superuser, **extra_fields):
        """
        """
        now = timezone.now()

        if not email:
            raise ValueError(('Users must have an email address'))
        if not username:
            raise ValueError(('The given username must be set'))
        email = self.normalize_email(email)  # @도메인에 대한 정규화만 진행 도메인소문자 자세한 설명: https://dev-mht.tistory.com/163
        try:
            del extra_fields['confirm_password']  # 확인 패스워드 삭제
        except KeyError:
            pass

        account = self.model(email=email, username=username,
                             is_staff=is_staff, is_active=True,
                             is_superuser=is_superuser, last_login=now,
                             date_joined=now, **extra_fields)

        account.set_password(password)
        account.save(using=self._db)
        return account

    def create_user(self, email, username, password=None, **extra_fields):
        return self._create_user(email, username, password, False, False, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        return self._create_user(email, username, password, True, True, **extra_fields)

class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=('email address'),
        max_length=255,
        unique=True,
    )

    username = models.CharField(('username'), max_length=30,
                                help_text=('Requierd. 30 characters or fewer. Letters, digits'
                                           ' and ./+/-/_ only'),
                                validators=[  # 정규식을 통한 특수문자 제외
                                    validators.RegexValidator(r'^[\w.+-]+$', ('Enter a valid username.'), 'invalid')
                                ])

    is_staff = models.BooleanField(('staff status'), default=False,
                                   help_text='Designates whether the user can log into this admin site')
    is_active = models.BooleanField(('active'), default=True,
                                    help_text='Designates whether this user should be treated as '
                                              'active. Unselect this instead of deleting accounts.')

    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    #썸네일
    thumbnail = ProcessedImageField(blank=True, upload_to="profile" , null=True, processors=[ResizeToFill(100,100)],
                                    format='JPEG', options={'quality': 80})

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    object = AccountManager()


    # 유저 모델에서 필드의 이름을 설명하는 string입니다 유니크 식별자로 사용
    USERNAME_FIELD = 'email'

    # createsuperuser 커맨드로 유저를 생성할 때 나타날 필드 이름 목록
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.username

    def get_email_id(self):
        """
        :return: Account id.
        """
        return self.email

    @property
    def photo_url(self):
        return '{}{}'.format(settings.MEDIA_URL, self.thumbnail)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User
        :param subject:
        :param message:
        :param from_email:
        :param kwargs:
        :return:
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
