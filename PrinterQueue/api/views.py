from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Printer, Job, PriorityQueue
from PrinterQueue.api.serializers import UserSerializer, PrinterSerializer, JobSerializer
from rest_framework.decorators import detail_route, list_route, api_view
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint for jobs
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class PrinterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows printers to be viewed or edited.
    """
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer


@api_view(['GET'])
def deploy_jobs(request):
    queue = PriorityQueue()
    jobs = Job.objects.all()
    completedjobs = []

    for job in jobs:
        queue.push(job.jobname, job.priority)

    for i in range(len(jobs)):
        completedjobs.append(queue.pop())
    return Response({"Response": completedjobs.__str__()})


