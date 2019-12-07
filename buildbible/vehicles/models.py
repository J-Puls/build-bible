from django.db import models
from PIL import Image
from datetime import date

class Vehicle(models.Model):
    MANUFACTURER_CHOICES = [
        # A
    ('Acura', 'Acura'),
    ('Alpha Romero', 'Alpha Romero'),
    ('Aston Martin', 'Aston Martin'),
    ('Audi', 'Audi'),
    # B
    ('Bentley', 'Bentley'),
    ('Buick', 'Buick'),
    ('Bmw', 'Bmw'),
    # C
    ('Cadillac', 'Cadillac'),
    ('Chevrolet', 'Chevrolet'),
    ('Chrysler', 'Chrysler'),
    ('Citroen', 'Citroen'),
    # D
    ('Daihatsu', 'Daihatsu'),
    ('Datsun', 'Datsun'),
    ('Dodge', 'Dodge'),
    # E
    ('Eagle', 'Eagle'),
    # F
    ('Ferrari', 'Ferrari'),
    ('Fiat', 'Fiat'),
    ('Ford', 'Ford'),
    # G
    ('Gmc', 'Gmc'),
    # H
    ('Holden', 'Holden'),
    ('Honda', 'Honda'),
    ('Hummer', 'Hummer'),
    ('Hyundai', 'Hyundai'),
    # I
    ('Infiniti', 'Infiniti'),
    # J
    ('Jaguar', 'Jaguar'),
    ('Jeep', 'Jeep'),
    # K
    ('Kia', 'Kia'),
    # L
    ('Lamborghini', 'Lamborghini'),
    ('Land Rover', 'Land Rover'),
    ('Lexus', 'Lexus'),
    ('Lotus', 'Lotus'),
    # M
    ('Maserati', 'Maserati'),
    ('Mazda', 'Mazda'),
    ('Mclaren', 'Mclaren'),
    ('Mercedes-Benz', 'Mercedes-Benz'),
    ('Mercury', 'Mercury'),
    ('Mg', 'Mg'),
    ('Mini', 'Mini'),
    ('Mitsubishi', 'Mitsubishi'),
    # N
    ('Nissan', 'Nissan'),
    # O
    ('Oldsmobile', 'Oldsmobile'),
    ('Opel', 'Opel'),
    # P
    ('Peugeot', 'Peugeot'),
    ('Plymouth', 'Plymouth'),
    ('Pontiac', 'Pontiac'),
    ('Porsche', 'Porsche'),
    # R
    ('Renault', 'Renault'),
    ('Rolls-Royce', 'Rolls-Royce'),
    # S
    ('Saab', 'Saab'),
    ('Scion', 'Scion'),
    ('Seat', 'Seat'),
    ('Shelby', 'Shelby'),
    ('Smart', 'Smart'),
    ('Subaru', 'Subaru'),
    ('Suzuki', 'Suzuki'),
    # T
    ('Tesla', 'Tesla'),
    ('Toyota', 'Toyota'),
    ('Triumph', 'Triumph'),
    # V
    ('Vauxhall', 'Vauxhall'),
    ('Volkswagen', 'Volkswagen'),
    ('Volvo', 'Volvo')
    ]
    manufacturer = models.TextField(choices=MANUFACTURER_CHOICES)
    model_name = models.CharField(max_length=150)
    chassis_code = models.CharField(max_length=20)
    current_year = date.today().year
    YEAR_CHOICES = [(i,i) for i in reversed(range(1901, current_year + 1))]
    production_start = models.IntegerField(choices=YEAR_CHOICES, default=current_year)
    production_end = models.IntegerField(choices=YEAR_CHOICES, default=current_year)
    def __str__(self):
        return f'{self.chassis_code} {self.manufacturer} {self.model_name} ({self.production_start}-{self.production_end})'
        

class VehicleProfile(models.Model):
    context = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    image = models.ImageField(default='default_vehicle.png', upload_to='vehicle_pics')

    def __str__(self):
        return f'{self.context.manufacturer} {self.context.model_name} {self.context.chassis_code} Profile'

    def save(self, *args, **kwargs):
        super(VehicleProfile, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image Preview'