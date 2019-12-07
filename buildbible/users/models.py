from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import piexif

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image Preview'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
        
    #     def crop_center(pil_img, crop_width, crop_height):
    #         img_width, img_height = pil_img.size
    #         return pil_img.crop(((img_width - crop_width) // 2,
    #                             (img_height - crop_height) // 2,
    #                             (img_width + crop_width) // 2,
    #                             (img_height + crop_height) // 2))

    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         width, height = img.size
    #         img = crop_center(img, width, height)
        
    #     if "exif" in img.info:
    #         exif_dict = piexif.load(img.info["exif"])

    #     if piexif.ImageIFD.Orientation in exif_dict["0th"]:
    #         orientation = exif_dict["0th"].pop(piexif.ImageIFD.Orientation)
    #         exif_bytes = piexif.dump(exif_dict)

    #         if orientation == 2:
    #             img = img.transpose(Image.FLIP_LEFT_RIGHT)
    #         elif orientation == 3:
    #             img = img.rotate(180)
    #         elif orientation == 4:
    #             img = img.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
    #         elif orientation == 5:
    #             img = img.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
    #         elif orientation == 6:
    #             img = img.rotate(-90, expand=True)
    #         elif orientation == 7:
    #             img = img.rotate(90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
    #         elif orientation == 8:
    #             img = img.rotate(90, expand=True)
    #         width, height = img.size
    #         img = crop_center(img, width, height)
    #         img.save(self.image.path, exif=exif_bytes)
    #     else:
    #         img.save(self.image.path)
