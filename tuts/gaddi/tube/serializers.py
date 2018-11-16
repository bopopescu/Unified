from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = ('firstname','emp_id', 'workinghours','experience')

		#displying all fields , fields = '__all__'