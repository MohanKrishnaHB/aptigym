from django.db import models


class CategoryLevel1(models.Model):
    title = models.CharField(
        max_length=20, unique=True)
    description = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


def create_default_category1():
    default_categoory = CategoryLevel1.objects.filter(title="other")
    if default_categoory.exists():
        return default_categoory[0]
    else:
        return CategoryLevel1(title="other").save()


class CategoryLevel2(models.Model):
    title = models.CharField(max_length=20, unique=True)
    category_level_1 = models.ForeignKey(
        CategoryLevel1, on_delete=models.SET(create_default_category1), related_name="sub_categories")

    def __str__(self):
        return self.title


def create_default_category2():
    default_categoory = CategoryLevel2.objects.filter(title="other")
    if default_categoory.exists():
        return default_categoory[0]
    else:
        return CategoryLevel2(title="other").save()


class Question(models.Model):
    question = models.TextField()
    has_question_image = models.BooleanField(default=False)
    question_image = models.ImageField(
        upload_to='images/question/', null=True, blank=True)
    solution = models.TextField()
    has_solution_image = models.BooleanField(default=False)
    solution_image = models.ImageField(
        upload_to='images/solution/', null=True, blank=True)
    category = models.ForeignKey(
        CategoryLevel2, on_delete=models.SET(create_default_category2), related_name="questions")
    created_on = models.DateField(auto_now=True)

    def __str__(self):
        return "Question {}".format(self.id)


class Options(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='options')
    option = models.CharField(max_length=100)
    has_image = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to='images/options/', null=True, blank=True)
    is_true = models.BooleanField(default=False)

    class Meta:
        unique_together = ['question', 'option']

    def __str__(self):
        return "question {} | option {}".format(self.question.id, self.id)
