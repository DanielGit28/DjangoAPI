from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *

# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

class ReactView(APIView):
    def get(self, request):
        output = [{"employee": output.employee,
                   "department": output.department}
                   for output in React.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
