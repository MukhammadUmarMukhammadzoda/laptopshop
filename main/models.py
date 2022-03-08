from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images')


    def __str__(self):
        return self.name


class Category(models.Model):
    
    category = models.CharField(max_length=100)


    def __str__(self):
        return self.category



class Product(models.Model):
    
    display_choice = (
        ('15.6','15.6'),
        ('14','14'),
        ('13.3', '13.3'),
        ('16','16'),
        ('17.2','17.2')
    )


    display_type_choice = (
        ('IPS', 'IPS'),
        ('Oled', 'Oled'),
        ('TN', 'TN'),
        ('Tft','Tft')
    )

    corpus_type = (
        ('Metall', 'Metall'),
        ('Plastik','Plastik'),
        ('Alyumin','Alyumin')
    )

    img = models.ImageField(upload_to="images")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    model = models.CharField(max_length=75)
    display_size = models.CharField(max_length=40,choices=display_choice)
    display_type = models.CharField(max_length=40,choices=display_type_choice)
    CPU = models.CharField(max_length=100)
    GPU = models.CharField(max_length=100)
    RAM = models.CharField(max_length=40)
    Hard = models.CharField(max_length=50)
    courpus = models.CharField(max_length=50,choices=corpus_type)
    colour = models.CharField(max_length=60)
    Batarey = models.CharField(max_length=40)
    Audio = models.CharField(max_length=50)
    price = models.CharField(max_length=60)
    old_price = models.CharField(max_length=50,blank=True, null=True)


    def __str__(self):
        return self.brand.name + '\t' +  self.model



