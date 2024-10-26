from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.response import Response
from .serializers import StudentSerializer 
from .models import Student  
from rest_framework.renderers import JSONRenderer
# Company ViewSet
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    @action(detail=True, methods=['get'])
    def employees(self, request, pk = None):
        try:
            company=Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exists!! Error '
            })


# Employee ViewSet
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

def student_detail(request):
    stu = Student.objects.get(id = 1)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
