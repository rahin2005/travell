from django.db import models
from accounts.models import CustomUser  # ارتباط با مدل کاربری
from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    STAR_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    name = models.CharField(max_length=100,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    manager_name = models.CharField(max_length=100)
    manager_phone = models.CharField(max_length=15,null=True,blank=True)
    hotel_phone=models.CharField(max_length=15,null=True,blank=True)
    bank_number = models.CharField(max_length=16,null=True,blank=True)
    features = models.TextField(null=True,blank=True)
    stars = models.IntegerField(choices=STAR_CHOICES, default=1)
    password = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.get_stars_display()}"
    
    


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='images', on_delete=models.CASCADE)  # اتصال به هتل
    image = models.ImageField(upload_to='hotel_images/')  # محل ذخیره‌سازی تصاویر
    description = models.CharField(max_length=255, blank=True)  # توضیح اختیاری برای تصویر

    def __str__(self):
        return f"Image for {self.hotel.name}"





class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # تغییر به CustomUser
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.user.username} for {self.hotel.name}"
    

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')  # لینک به هتل
    name = models.CharField(max_length=100)  # مثلا "سوئیت VIP"
    price = models.DecimalField(max_digits=10, decimal_places=2)  # قیمت هر شب
    capacity = models.IntegerField()  # چند نفر می‌تونن توی اتاق بمونن
    features = models.TextField(blank=True)  # امکانات خاص
    available = models.BooleanField(default=True)  # آیا اتاق در دسترسه؟

    def __str__(self):
        return f"{self.name} - {self.hotel.name}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # کاربری که رزرو کرده
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # کدوم اتاق؟
    check_in = models.DateField()  # تاریخ ورود
    check_out = models.DateField()  # تاریخ خروج
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # مبلغ کل رزرو

    def __str__(self):
        return f"{self.user.username} - {self.room.name} - {self.check_in} to {self.check_out}"