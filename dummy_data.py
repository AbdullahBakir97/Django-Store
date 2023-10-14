import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()

from faker import Faker
import random
from products.models import Product , Brand , Review


def add_brands(n):
    fake = Faker()
    images = ('1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg',)

    for x in range(n):
        Brand.objects.create(
            name = fake.name() ,
            image = f"brands/{images[random.randint(0,9)]}"
        )
        
    print(f'{n} Brands was created successfully')

def add_products(n):
    pass


add_brands(3)