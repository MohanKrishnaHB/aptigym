from django.db import models
from student.models import Student
from question.models import Question


class Test(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    no_of_questions = models.IntegerField()
    total_duration = models.TimeField(auto_now=False, auto_now_add=False)
    negative_marking = models.BooleanField(default=False)
    commence_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    stop_commenceing_after = models.DateTimeField(
        auto_now=False, auto_now_add=False)
    show_score = models.BooleanField(default=False)
    show_answers = models.BooleanField(default=False)


class TestPartition(models.Model):
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE, related_name="partitions")
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    no_of_questions = models.IntegerField()


class TestQuestions(models.Model):
    partition = models.ForeignKey(
        Test, on_delete=models.CASCADE, related_name="questions")
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="partitions")


class StudentTest(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="tests")
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE, related_name="students")
    status = models.CharField(max_length=20, default="not_attended")


class StudentQuestion(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="questions")
    question = models.ForeignKey(
        TestQuestions, on_delete=models.CASCADE, related_name="students")
    status = models.CharField(max_length=20, default="not_attended")
    points = models.DecimalField(max_digits=3, decimal_places=2)
    duration = models.TimeField(auto_now=False, auto_now_add=False)
