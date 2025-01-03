from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.utils import timezone

class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, name, phone, password, **extra_fields):
        for field, value in zip(['email', 'name', 'phone'], [email, name, phone]):
            if not value:
                raise ValueError(f'The {field} value must be set.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, phone, password, **extra_fields)

    def create_superuser(self, email, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields['is_staff'] or not extra_fields['is_superuser']:
            raise ValueError('Superuser must have is_staff=True and is_superuser=True.')

        return self._create_user(email, name, phone, password, **extra_fields)

class Account(AbstractBaseUser,PermissionsMixin):
    
    USER_ROLES = [
        ('admin', 'admin'),
        ('instructor', 'instructor'),
        ('student', 'student'),
    ]
    
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    role = models.CharField(choices=USER_ROLES, default='student',max_length=20)
    avatar = models.ImageField(blank=True, null=True,upload_to='avatars')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']
    
    def has_perm(self, perm, obj=None):
        """Return True if the user has a specific permission."""
        if self.role == 'admin' or self.role == 'instructor':
            return True
        else:
            return False

    def has_module_perms(self, app_label):
        """Return True if the user has permissions for the app."""
        return True

    def __str__(self):
        return self.email