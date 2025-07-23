from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    CITY_CHOICES = [
    ('vinnytsia', 'Вінниця'),
    ('lutsk', 'Луцьк'),
    ('dnipro', 'Дніпро'),
    ('donetsk', 'Донецьк'),
    ('zhytomyr', 'Житомир'),
    ('uzhhorod', 'Ужгород'),
    ('zaporizhzhia', 'Запоріжжя'),
    ('ivano-frankivsk', 'Івано-Франківськ'),
    ('kyiv', 'Київ'),
    ('kropyvnytskyi', 'Кропивницький'),
    ('lviv', 'Львів'),
    ('mykolaiv', 'Миколаїв'),
    ('odesa', 'Одеса'),
    ('poltava', 'Полтава'),
    ('rivne', 'Рівне'),
    ('sumy', 'Суми'),
    ('ternopil', 'Тернопіль'),
    ('kharkiv', 'Харків'),
    ('kherson', 'Херсон'),
    ('khmelnytskyi', 'Хмельницький'),
    ('cherkasy', 'Черкаси'),
    ('chernivtsi', 'Чернівці'),
    ('chernihiv', 'Чернігів'),

    # Надіюсь колись ми зможемо створити тут івент
    ('simferopol', 'Сімферополь'),
    ('yalta', 'Ялта'),
    ('kerch', 'Керч'),
    ('feodosiya', 'Феодосія'),
    ('yevpatoria', 'Євпаторія'),
    ('saki', 'Саки'),
    ('sevastopol', 'Севастополь'),
]
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    date = models.DateTimeField()
    location_city = models.CharField(choices=CITY_CHOICES, max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organizer")
    user = models.ManyToManyField(User, related_name="joined_event")
    age_limit = models.BooleanField(default=False)
    price = models.FloatField(null=True)
    image = models.ImageField(upload_to="event_image/", null=True)
    
