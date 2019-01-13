from django.db import models
class sport_kids(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=False)
    photo2 = models.FileField(blank=False)
    desc = models.TextField(max_length=700)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=20)
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class jeans_kids(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=False)
    photo2 = models.FileField(blank=False)
    desc = models.TextField(max_length=700)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=20)
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class shirt_kids(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=False)
    photo2 = models.FileField(blank=False)
    desc = models.TextField(max_length=700)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=20)
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class tshirt_kids(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=False)
    photo2 = models.FileField(blank=False)
    desc = models.TextField(max_length=700)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=20)
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class lehgas_choli(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=False)
    photo2 = models.FileField(blank=False)
    desc = models.TextField(max_length=700)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=20)
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Western_wear(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=False)
    photo2 = models.FileField(blank=False)
    desc = models.TextField(max_length=700)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=20)
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class shari(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=False)
    photo2 = models.FileField(blank=False)
    desc = models.TextField(max_length=700)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=20)
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class servani(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=True)
    photo2 = models.FileField(blank=True)
    desc = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class kurtas(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=True)
    photo2 = models.FileField(blank=True)
    desc = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class formal_pant(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=True)
    photo2 = models.FileField(blank=True)
    desc = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class casual_pant(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=True)
    photo2 = models.FileField(blank=True)
    desc = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class sweater_men(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=True)
    photo2 = models.FileField(blank=True)
    desc = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class jackets(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=True)
    photo2 = models.FileField(blank=True)
    desc = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class sport_wear(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=True)
    photo2 = models.FileField(blank=True)
    desc = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class jeans(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=True)
    photo2 = models.FileField(blank=True)
    desc = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class casualshirt(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=True)
    photo2 = models.FileField(blank=True)
    desc = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class tshirt(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=True)
    photo2 = models.FileField(blank=True)
    desc = models.TextField(max_length=700)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class formalshirts(models.Model):
    name = models.CharField(max_length=100)
    photo1 = models.FileField(blank=True)
    photo2 = models.FileField(blank=True)
    desc = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    availibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   # tshirt = models.ForeignKey('tshirt', null=False)
    def __str__(self):
        return self.name



