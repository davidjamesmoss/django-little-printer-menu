from django.db import models


class SetupManager(models.Manager):
    def get(self):
        return super(SetupManager, self).get_or_create(pk=1)[0]


class Setup(models.Model):
    menu_title = models.CharField('Menu Title', max_length=255, blank=True,
                                  null=True, help_text='Optional. Appears at \
                                  the top of your menu.')
    printer_key = models.CharField('Printer Key', max_length=20, null=True,
                                   help_text='Required. It will be something \
                                   like ABCDE1FGHIJ2.')

    values = SetupManager()


class Dish(models.Model):
    title = models.CharField('Dish', max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Dishes'


class Menu(models.Model):
    day_choices = (
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
    )

    day = models.CharField('Day', max_length=3, choices=day_choices,
                           default='mon')
    dish = models.ForeignKey(Dish, null=True, blank=True)
    alternative = models.TextField('Alternative', blank=True)

    def __unicode__(self):
        if self.alternative:
            return self.alternative.strip()
        elif self.dish:
            return self.dish.title.strip()
        else:
            return 'Mystery dish'
