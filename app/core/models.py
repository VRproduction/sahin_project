from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Service(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'services')
    duration = models.IntegerField(null = True, blank = True, verbose_name = 'Xidmət müddəti (gün)')
    price = models.IntegerField(null = True, blank = True, verbose_name = 'Xidmət haqqı (saat başına)')

    def __str__(self) -> str:
        return self.title 
    
    class Meta:
        verbose_name = 'Servis'
        verbose_name_plural = 'Servislər'

    def get_absolute_url(self):
        return reverse("service-detail", args=[str(self.pk)])

class Project(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'projects')
    location = models.CharField(max_length = 50)
    sector = models.CharField(max_length = 50)
    scope_of_work = models.BigIntegerField()
    location = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.title 
    
    class Meta:
        verbose_name = 'Proyekt'
        verbose_name_plural = 'Proyektlər'

    # def get_absolute_url(self):
    #     return reverse("service-detail", args=[str(self.pk)])

class About(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'about')
    active_project = models.IntegerField()
    control_rate = models.IntegerField()
    
    def __str__(self) -> str:
        return self.title 
    
    class Meta:
        verbose_name = 'Haqqımızda'
        verbose_name_plural = 'Haqqımızda'

class Punkt(models.Model):
    title = models.CharField(max_length = 200)
    about = models.ForeignKey(About, on_delete = models.CASCADE, related_name = 'punkts')

    def __str__(self) -> str:
        return self.title 
    
    class Meta:
        verbose_name = 'Punkt'
        verbose_name_plural = 'Punktlar'

class WhyChooseUs(models.Model):
    completed_projects = models.BigIntegerField()
    turnover_price = models.BigIntegerField()
    control_rate = models.BigIntegerField()
    active_projects = models.BigIntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return f"Niyə bizi seçirlər"
    
    class Meta:
        verbose_name = 'Niyə bizi seçirlər'
        verbose_name_plural = 'Niyə bizi seçirlər'

class WhyChooseUsPunkt(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    model = models.ForeignKey(WhyChooseUs, on_delete = models.CASCADE, related_name = 'punkts')

    def __str__(self) -> str:
        return self.title 
    
    class Meta:
        verbose_name = 'Punkt'
        verbose_name_plural = 'Punktlar'

class Process(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self) -> str:
        return f"Biz necə çalışırıq"
    
    class Meta:
        verbose_name = 'Biz necə çalışırıq'
        verbose_name_plural = 'Biz necə çalışırıq'

class ProcessPunkt(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    model = models.ForeignKey(Process, on_delete = models.CASCADE, related_name = 'punkts')

    def __str__(self) -> str:
        return self.title 
    
    class Meta:
        verbose_name = 'Punkt'
        verbose_name_plural = 'Punktlar'

class Gallery(models.Model):
    image = models.ImageField(upload_to = 'gallery')
    title = models.CharField(max_length = 200)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Şəkil'
        verbose_name_plural = 'Qalereya'

class News(models.Model):
    title = models.CharField(max_length = 500)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to = 'news')
    created = models.DateTimeField(auto_now_add = True)
    is_main_page  = models.BooleanField(default = False, verbose_name = "Əsas səhifədə görünsün?")

    def __str__(self):
        return ('%s') % (self.title)

    class Meta:
        verbose_name = "Xəbər"
        verbose_name_plural = "Xəbərlər"

    # def get_absolute_url(self):
    #     return reverse("blog-detail", args=[str(self.pk)])
        
class Team(models.Model):
    full_name = models.CharField(max_length = 100)
    position = models.CharField(max_length = 100)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to = 'team', null = True)


    def __str__(self):
        return ('%s') % (self.full_name)

    class Meta:
        verbose_name = "Üzv"
        verbose_name_plural = "Komanda üzvləri"
