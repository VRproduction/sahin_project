from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

class GeneralSettings(models.Model):
    site_title = models.CharField(
        max_length=200, verbose_name="Saytın başlığı")
    adress = models.CharField(max_length=1500, verbose_name="Ünvan", null=True, blank=True)
    email = models.EmailField(blank = True)
    phone_number = models.CharField(max_length = 50)
    g_adress = models.CharField(
        max_length=1500, verbose_name="Google Map linki", null=True, blank=True)
    g_adress_iframe = models.TextField(
        verbose_name="Google Map Iframe linki", null=True, blank=True)
    logo = models.FileField(blank=True, upload_to="general_settings_logo")
    favicon = models.FileField(blank=True, null=True, upload_to="general_settings_favicon")
    footer_logo = models.FileField(help_text="Footer logo", blank=True, null=True, upload_to="general_settings_footer_logo")
    footer_slogan = models.TextField(null = True, blank = True)
    copyright_title = models.CharField(max_length = 100, blank = True)
    copyright_link = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return ('%s') % (self.site_title)

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "General Settings"

class Hero(models.Model):
    slogan = models.CharField(max_length = 200, null = True)
    title = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'hero')
    project_for_year = models.IntegerField(null = True, blank = True, verbose_name = 'Proyekt / Il')
    turnover = models.BigIntegerField(null = True, blank = True, verbose_name = 'İllik dövriyyə')

    def __str__(self) -> str:
        return self.title 
    
    class Meta:
        verbose_name = 'Ana səhifə | Əsas hissə'
        verbose_name_plural = 'Ana səhifə | Əsas hissə'

    # def get_absolute_url(self):
    #     return reverse("service-detail", args=[str(self.pk)])

class Service(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(blank=True, null=True, unique = True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'services')

    def __str__(self) -> str:
        return self.title 
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Servis'
        verbose_name_plural = 'Servislər'

    def get_absolute_url(self):
        return reverse("service-detail", args=[str(self.slug)])

class Project(models.Model):
    title = models.CharField(max_length = 200)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to = 'projects')
    location = models.CharField(max_length = 50)
    sector = models.CharField(max_length = 50)
    technology = models.CharField(max_length = 50, null = True)
    scope_of_work = models.BigIntegerField()
    completed = models.DateField(null = True)
    show_detail_info = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.title 
    
    class Meta:
        verbose_name = 'Proyekt'
        verbose_name_plural = 'Proyektlər'

    def get_absolute_url(self):
        return reverse("project-detail", args=[str(self.pk)])

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
    slug = models.SlugField(blank=True, null=True, unique = True)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to = 'news')
    created = models.DateTimeField(auto_now_add = True)
    is_main_page  = models.BooleanField(default = False, verbose_name = "Əsas səhifədə görünsün?")

    def __str__(self):
        return ('%s') % (self.title)

    class Meta:
        verbose_name = "Xəbər"
        verbose_name_plural = "Xəbərlər"
        ordering = ["-created",]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("news-detail", args=[str(self.slug)])
        
class Team(models.Model):
    full_name = models.CharField(max_length = 100)
    position = models.CharField(max_length = 100)
    description = RichTextUploadingField(null = True, blank = True)
    image = models.ImageField(upload_to = 'team', null = True, verbose_name = 'image (417x603)px')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)


    def __str__(self):
        return ('%s') % (self.full_name)

    class Meta:
        verbose_name = "Üzv"
        verbose_name_plural = "Komanda üzvləri"
        ordering = ['order'] 

    def save(self, *args, **kwargs):
        if not self.pk:
            max_order = Team.objects.aggregate(models.Max('order'))['order__max'] or 0
            self.order = max_order + 1
        super().save(*args, **kwargs)

class Contact(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    number = models.CharField(max_length = 50)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return ('%s') % (self.name)

    class Meta:
        verbose_name = "Mesaj"
        verbose_name_plural = "Mesajlar"