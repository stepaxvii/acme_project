from django.db import models

from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=20
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        blank=True,
        help_text='Необязательное поле',
        max_length=20
    )
    birthday = models.DateField(
        verbose_name='Дата рождения',
        validators=(real_age,)
    )

    class Meta:
        verbose_name = 'День рождения'
        verbose_name_plural = 'дни рождения'
        ordering = ('id',)
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constaint',
            ),
        )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
