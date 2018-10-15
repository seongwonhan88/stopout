from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    school = models.ForeignKey(
        'School',
        on_delete=models.SET_NULL,
        null=True,
    )
    student_name = models.CharField(max_length=100)
    friends = models.ManyToManyField(
        'self'
    )

    def __str__(self):
        return self.student_name

    def friends_list(self):
        return self.friends.all()
