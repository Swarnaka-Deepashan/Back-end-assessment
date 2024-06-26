from django.db import models

# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length=255)
    year = models.IntegerField()
    student_id = models.IntegerField()
    first_name = models.CharField(max_length=255)

    last_name = models.CharField(max_length=255)
    year_level = models.IntegerField()
    student_class = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)

    answers = models.CharField(max_length=255)
    correct_answers = models.CharField(max_length=255)
    question_number = models.IntegerField()
    subject_contents = models.CharField(max_length=255)

    assessment_areas = models.CharField(max_length=255)
    sydney_correct_count_percentage = models.FloatField()
    sydney_average_score = models.FloatField()
    sydney_participants = models.IntegerField()

    student_score = models.FloatField()
    student_total_assessed = models.IntegerField()
    student_area_assessed_score = models.FloatField()
    total_area_assessed_score = models.FloatField()

    participant = models.IntegerField()
    correct_answer_percentage_per_class = models.FloatField()
    average_score = models.FloatField()
    school_percentile = models.IntegerField()

    sydney_percentile = models.IntegerField()
    strength_status = models.CharField(max_length=255)
    high_distinct_count = models.IntegerField()
    distinct_count = models.IntegerField()

    credit_count = models.IntegerField()
    participant_count = models.IntegerField()
    award = models.CharField(max_length=255)



