from django.db import models


class CategoryLevel1(models.Model):
    title = models.CharField(
        max_length=20, unique=True)
    description = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


def create_default_category1():
    default_categoory = CategoryLevel1.objects.filter(title="not assigned")
    if default_categoory.exists():
        return default_categoory[0]
    else:
        return CategoryLevel1(title="not assigned").save()


class CategoryLevel2(models.Model):
    title = models.CharField(max_length=20, unique=True)
    category_level_1 = models.ForeignKey(
        CategoryLevel1, default=0, on_delete=models.SET(create_default_category1))

    def __str__(self):
        return self.title


class question
