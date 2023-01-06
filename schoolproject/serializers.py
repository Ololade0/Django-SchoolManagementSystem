from rest_framework import serializers

from playground.models import School, Student, Course, Result


class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'school_name', 'school_location', 'school_email']


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'age', 'date_birth', 'gender_choices', 'school']


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_code', 'course_status', 'course_description', 'school', 'student']


class ResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['id', 'score', 'grade', 'course', 'student']
