from django.db import models

# Create your models here.
import os
from PIL import Image
from django.db.models import Q


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_about_us_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}{ext}"
    # final_name = f"{instance.id}-{instance.title}{ext}"
    return f"aboutus/{final_name}"


def upload_avatar_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}{ext}"
    # final_name = f"{instance.id}-{instance.title}{ext}"
    return f"avatar/{final_name}"

def upload_project_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}{ext}"
    # final_name = f"{instance.id}-{instance.title}{ext}"
    return f"project/{final_name}"

def upload_propic_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}{ext}"
    # final_name = f"{instance.id}-{instance.title}{ext}"
    return f"propic/{final_name}"

def upload_artpic_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}{ext}"
    # final_name = f"{instance.id}-{instance.title}{ext}"
    return f"artpic/{final_name}"


def upload_articles_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}{ext}"
    # final_name = f"{instance.id}-{instance.title}{ext}"
    return f"articles/{final_name}"
def upload_file_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}{ext}"
    # final_name = f"{instance.id}-{instance.title}{ext}"
    return f"files/{final_name}"
def upload_grade_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}{ext}"
    # final_name = f"{instance.id}-{instance.title}{ext}"
    return f"grades/{final_name}"
# class YadManager(models.Manager):
#
#    def search(self, query):
#         lookup = (
#                 Q(name__icontains=query) |
#                 Q(family__icontains=query)
#
#          )
#         yadi=Yad.objects.filter(lookup).distinct()
#         return yadi




class About(models.Model):
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    title = models.CharField(max_length=150, verbose_name='موضوع', default='درباره ما')
    subject = models.TextField(verbose_name='موضوع شرکت', null=True, blank=True)
    short_description = models.TextField(verbose_name='توضیحات کوتا', null=True, blank=True)
    long_description = models.TextField(verbose_name='توضیحات بلند', null=True, blank=True)
    address = models.TextField(verbose_name='آدرس', null=True, blank=True)
    email = models.TextField(verbose_name='ایمیل', null=True, blank=True)
    phone = models.TextField(verbose_name='تلفن', null=True, blank=True)
    master_image = models.ImageField(upload_to=upload_about_us_image_path, null=True, blank=True, verbose_name='تصویر اصلی')
    # objects=YadManager()
    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'انواع درباره ما'

    def __str__(self):
        return self.title
        # return "%s %s" % (self.name, self.family)
    # def get_absolute_url(self):
    #     return f"/yadbood/{self.id}"

    def save(self, *args, **kwargs):
        super().save()
        picpath=self.master_image.path
        img = Image.open(picpath)
        width, height = img.size  # Get dimensions
        w=691
        h=461

        if width/height > w/h:
            w2=w*height/h
            left=(width-w2)/2
            right=left+w2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height < w/h:
            h2=h*width/w
            left=0
            right=width
            top=(height-h2)/2
            bottom=top+h2
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height == w/h:
            img.thumbnail((w, h))
            img.save(picpath)


class Team(models.Model):
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    super = models.BooleanField(default=True, verbose_name='عضویت هیئت مدیره')
    name = models.CharField(max_length=150, verbose_name='نام')
    position = models.CharField(max_length=150, verbose_name='جایگاه')
    about_me = models.CharField(max_length=150, verbose_name=' درباره من',null=True, blank=True,)
    telegram = models.CharField(max_length=150, verbose_name=' لینک تلگرام',null=True, blank=True,)
    instagram = models.CharField(max_length=150, verbose_name=' لینک اینستاگرام',null=True, blank=True,)
    avatar = models.ImageField(upload_to=upload_avatar_image_path, null=True, blank=True, verbose_name='تصویر پروفایل')

    class Meta:
        verbose_name = 'فرد'
        verbose_name_plural = 'افراد'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save()
        picpath=self.avatar.path
        img = Image.open(picpath)
        width, height = img.size  # Get dimensions
        w=300
        h=300

        if width/height > w/h:
            w2=w*height/h
            left=(width-w2)/2
            right=left+w2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height < w/h:
            h2=h*width/w
            left=0
            right=width
            top=(height-h2)/2
            bottom=top+h2
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height == w/h:
            img.thumbnail((w, h))
            img.save(picpath)


class Projects(models.Model):
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    name = models.CharField(max_length=150, verbose_name='نام پروزه')
    subject = models.CharField(max_length=150, verbose_name='موضوع پروژه')
    # about_project = models.CharField(max_length=150, verbose_name=' درباره پروژه',null=True, blank=True,)
    about_project=models.TextField(verbose_name='درباره پروژه', null=True, blank=True)
    p_picture = models.ImageField(upload_to=upload_project_image_path, null=True, blank=True, verbose_name='تصویر پروفایل')
    timep = models.CharField(max_length=150, verbose_name='زمان پروژه', null=True, blank=True)
    kinde = models.CharField(max_length=150, verbose_name='نوع پوژه', null=True, blank=True)
    statusp = models.CharField(max_length=150, verbose_name='وضعیت', null=True, blank=True)
    zirbana = models.CharField(max_length=150, verbose_name='زیر بنا', null=True, blank=True)
    area = models.CharField(max_length=150, verbose_name='مساحت', null=True, blank=True)
    price = models.CharField(max_length=150, verbose_name='مبلغ پروژه', null=True, blank=True)
    locationp = models.CharField(max_length=150, verbose_name='محل پروژه', null=True, blank=True)
    employer = models.CharField(max_length=150, verbose_name='کارفرما', null=True, blank=True)
    engineer=models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE ,verbose_name='مهندس پروژه')

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.p_picture.path)
        width, height = img.size  # Get dimensions
        w=1024
        h=614
        picpath=self.p_picture.path
        if width/height > w/h:
            w2=w*height/h
            left=(width-w2)/2
            right=left+w2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height < w/h:
            h2=h*width/w
            left=0
            right=width
            top=(height-h2)/2
            bottom=top+h2
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height == w/h:
            img.thumbnail((w, h))
            img.save(picpath)


class ProjectPicture(models.Model):
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    pimage = models.ImageField(upload_to=upload_propic_image_path, null=True, blank=True, verbose_name='تصویر ')
    # pimage =ResizedImageField(size=[300, 120], upload_to=upload_propic_image_path, blank=True, null=True,verbose_name='تصویر ')
    project=models.ForeignKey(Projects, blank=True, null=True, on_delete=models.CASCADE ,verbose_name='پروژه')

    # objects=YadManager()
    class Meta:
        verbose_name = 'تصویر پروژه'
        verbose_name_plural = 'تصاویر پروژه'

    def __str__(self):
        t=str(self.id)
        return t
        # return "%s %s" % (self.name, self.family)
    # def get_absolute_url(self):
    #     return f"/yadbood/{self.id}"

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.pimage.path)
        width, height = img.size  # Get dimensions
        w=10240
        h=6140
        picpath=self.pimage.path
        if width/height > w/h:
            w2=w*height/h
            left=(width-w2)/2
            right=left+w2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height < w/h:
            h2=h*width/w
            left=0
            right=width
            top=(height-h2)/2
            bottom=top+h2
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height == w/h:
            img.thumbnail((w, h))
            img.save(picpath)


class Customer(models.Model):
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    name = models.CharField(max_length=150, verbose_name='نام مشتری')
    cimage = models.ImageField(upload_to=upload_propic_image_path, null=True, blank=True, verbose_name='تصویر ')


    # objects=YadManager()
    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتری ها'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.cimage.path)
        width, height = img.size  # Get dimensions
        w=150
        h=150
        picpath=self.cimage.path
        if width/height > w/h:
            w2=w*height/h
            left=(width-w2)/2
            right=left+w2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height < w/h:
            h2=h*width/w
            left=0
            right=width
            top=(height-h2)/2
            bottom=top+h2
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height == w/h:
            img.thumbnail((w, h))
            img.save(picpath)


class Services(models.Model):
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    name1 = models.CharField(default="",max_length=50,null=True, blank=True, verbose_name='1عنوان')
    discription1 = models.CharField(default="",max_length=150, verbose_name='1توضیحات')

    name2 = models.CharField(default="",max_length=50,null=True, blank=True, verbose_name='2عنوان')
    discription2 = models.CharField(default="",max_length=150, verbose_name='2توضیحات')

    name3 = models.CharField(default="",max_length=50,null=True, blank=True, verbose_name='عنوان3')
    discription3 = models.CharField(default="",max_length=150,null=True, blank=True, verbose_name='3توضیحات')

    name4 = models.CharField(default="",max_length=50,null=True, blank=True, verbose_name='4عنوان')
    discription4 = models.CharField(default="",max_length=150,null=True, blank=True, verbose_name='4توضیحات')

    class Meta:
        verbose_name = 'خدمت'
        verbose_name_plural = 'خدمات'

    def __str__(self):
        return self.name1



class Articles(models.Model):
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    is_article = models.BooleanField(default=True, verbose_name='مقاله است')
    is_tips = models.BooleanField(default=False, verbose_name='نکات و تجربه است')
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    name = models.CharField(max_length=150, verbose_name='عنوان مقاله')
    time = models.CharField(max_length=150, verbose_name='زمان مقاله', null=True, blank=True)
    category = models.CharField(max_length=150, verbose_name='دسته بندی')
    shorttext = models.CharField(default="",max_length=250, verbose_name='متن کوتاه')
    text=models.TextField(verbose_name='متن مقاله', null=True, blank=True)
    image1 = models.ImageField(upload_to=upload_articles_image_path, null=True, blank=True, verbose_name='تصویر کوچک مقاله')
    image2 = models.ImageField(upload_to=upload_articles_image_path, null=True, blank=True, verbose_name='تصویر بزرگ مقاله')



    # engineer=models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE ,verbose_name='مهندس پروژه')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save()
        picpath=self.image1.path
        img = Image.open(picpath)
        width, height = img.size  # Get dimensions
        w=1024
        h=614

        if width/height > w/h:
            w2=w*height/h
            left=(width-w2)/2
            right=left+w2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height < w/h:
            h2=h*width/w
            left=0
            right=width
            top=(height-h2)/2
            bottom=top+h2
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height == w/h:
            img.thumbnail((w, h))
            img.save(picpath)

        picpath=self.image2.path
        img = Image.open(picpath)
        width, height = img.size  # Get dimensions
        w=3648
        h=2336

        if width/height > w/h:
            w2=w*height/h
            left=(width-w2)/2
            right=left+w2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height < w/h:
            h2=h*width/w
            left=0
            right=width
            top=(height-h2)/2
            bottom=top+h2
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height == w/h:
            img.thumbnail((w, h))
            img.save(picpath)



class ArticlesFile(models.Model):
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    name = models.CharField(max_length=150, verbose_name='نام فایل')
    afile = models.FileField(upload_to=upload_file_path, null=True, blank=True, verbose_name='فایل ')
    article=models.ForeignKey(Articles, blank=True, null=True, on_delete=models.CASCADE ,verbose_name='مقاله')

    # objects=YadManager()
    class Meta:
        verbose_name = 'فایل مقاله'
        verbose_name_plural = 'فایل های مقاله ها'

    def __str__(self):
        t=str(self.name)
        return t
        # return "%s %s" % (self.name, self.family)
    # def get_absolute_url(self):
    #     return f"/yadbood/{self.id}"


class ArticlesPicture(models.Model):
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    aimage = models.ImageField(upload_to=upload_artpic_image_path, null=True, blank=True, verbose_name='تصویر ')
    # pimage =ResizedImageField(size=[300, 120], upload_to=upload_propic_image_path, blank=True, null=True,verbose_name='تصویر ')
    article=models.ForeignKey(Articles, blank=True, null=True, on_delete=models.CASCADE ,verbose_name='مقاله')

    # objects=YadManager()
    class Meta:
        verbose_name = 'تصویر مقاله'
        verbose_name_plural = 'تصاویر مقاله ها'

    def __str__(self):
        t=str(self.id)
        return t
        # return "%s %s" % (self.name, self.family)
    # def get_absolute_url(self):
    #     return f"/yadbood/{self.id}"

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.aimage.path)
        width, height = img.size  # Get dimensions
        w=512
        h=307
        picpath=self.aimage.path
        if width/height > w/h:
            w2=w*height/h
            left=(width-w2)/2
            right=left+w2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height < w/h:
            h2=h*width/w
            left=0
            right=width
            top=(height-h2)/2
            bottom=top+h2
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height == w/h:
            img.thumbnail((w, h))
            img.save(picpath)






class Grades(models.Model):
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    name = models.CharField(max_length=150, verbose_name='نام گواهینامه')
    gimage = models.ImageField(upload_to=upload_grade_path, null=True, blank=True, verbose_name='تصویر ')


    # objects=YadManager()
    class Meta:
        verbose_name = 'گواهینامه'
        verbose_name_plural = 'گواهینامه ها'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save()
        picpath=self.gimage.path
        img = Image.open(picpath)
        width, height = img.size  # Get dimensions
        w=210
        h=297

        if width/height > w/h:
            w2=w*height/h
            left=(width-w2)/2
            right=left+w2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height < w/h:
            h2=h*width/w
            left=0
            right=width
            top=(height-h2)/2
            bottom=top+h2
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(picpath)

        if width/height == w/h:
            img.thumbnail((w, h))
            img.save(picpath)


class Test(models.Model):
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    super = models.BooleanField(default=True, verbose_name='ویژه / غیر ویژه')
    name = models.CharField(max_length=150, verbose_name='نام')

    class Meta:
        verbose_name = 'test'
        verbose_name_plural = 'tests'

    def __str__(self):
        return self.name

