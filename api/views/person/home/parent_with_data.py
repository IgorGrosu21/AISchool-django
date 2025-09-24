from api.models import Parent

from .student_with_data import student_with_data

def parent_with_data(parent: Parent):
  students = parent.students.prefetch_related(
    'groups__lessons',
    'notes__specific_lesson__lesson__subject'
  ).all()

  parent.students = [student_with_data(student) for student in students]

  return parent