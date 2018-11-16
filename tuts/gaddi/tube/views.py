from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from bokeh.resources import CDN
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components


from matplotlib import numpy
import numpy as np

# Create your views here.
from rest_framework import viewsets

from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeView(viewsets.ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

def chart1_view(request):

	return render(request, 'chart.html', {})
	
def chart_view(request):

	return render(request, 'index.html', {})


def simple_chart(request):
	plot = figure()


	plot.circle(Employee.objects.values_list('emp_id', flat=True),Employee.objects.values_list('workinghours', flat=True),	size = 10, color = "red", alpha = 0.5)



	script, div = components(plot,CDN)

	return render(request, "simple_chart.html",  {'the_script': script, 'the_div': div})



def index(request):
	x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
	y0 = [i**2 for i in x]
	y1 = [10**i for i in x]
	y2 = [10**(i**2) for i in x]
		
	p = figure(
   		tools="pan,box_zoom,reset,save",
   		y_axis_type="log", y_range=[0.001, 10**11], title="log axis example",
   		x_axis_label='sections', y_axis_label='particles'
	)
	p.line(x, x, legend="y=x")
	p.circle(x, x, legend="y=x", fill_color="white", size=8)
	p.line(x, y0, legend="y=x^2", line_width=3)
	p.line(x, y1, legend="y=10^x", line_color="red")
	p.circle(x, y1, legend="y=10^x", fill_color="red", line_color="red", size=6)
	p.line(x, y2, legend="y=10^x^2", line_color="orange", line_dash="4 4")

	script, div = components(p, CDN)

	#feed this to django template

	return render_to_response( 'bokeh.html',
            {'script' : script , 'div' : div} )
# 		