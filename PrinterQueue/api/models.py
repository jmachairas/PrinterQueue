from django.db import models
from heapq import heappush, heappop


class User(models.Model):
    url = models.URLField();
    username = models.CharField(max_length=100)
    email = models.EmailField()


class Job(models.Model):
    jobname = models.CharField(max_length=100)
    jobid = models.IntegerField(default=1)
    description = models.CharField(max_length=100)
    incolor = models.BooleanField(default=False)
    copies = models.IntegerField(default=1)
    orientation = models.CharField(max_length=20)
    duplex = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)


class Printer(models.Model):
    devicename = models.CharField(max_length=100)
    deviceid = models.IntegerField(default=1)
    description = models.CharField(max_length=100)
    colorcapable = models.BooleanField(default=False)
    duplex = models.BooleanField(default=False)
    copies = models.IntegerField(default=1)
    users = []


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heappop(self._queue)[-1]

