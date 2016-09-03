Initial Django REST Infrastructure for managing Printer(s) Job Queue(s)

This project currently supports adding new users, printers, and jobs; however currently the jobs are just matched to a single 
Priority Queue. Authenticating with credentials (admin, password123) allow you to perform all these operations, direct mapping 
from specific users to certain printer(s) is not supported yet. Basically the design was started in a fashion to support managing
multiple Printers in a more sophisticated way in the future. 

Installing the Printer Queue
  git clone https://github.com/jmachairas/PrinterQueue.git
  cd PrinterQueue
  pip install django
  pip install djangorestframework
  
Initializing DB
  python manage.py makemigrations
  python manage.py migrate
  
Running the Server
  python manage.py runserver
  
Running the Tests
  python manage.py test
  
Interacting with the Server 
  Use the web browsable api 
      available by going to the api endpoint printed from runserver command above (i.e. http://127.0.0.1:8000/)
      Use the interface at http://127.0.0.1:8000/users to create or edit users for the system
      Use the interface at http://127.0.0.1:8000/printers to add or edit new printers to the system
      Use the interface at http://127.0.0.1:8000/jobs to add or edit jobs with desired priority
  Use curl or http commmandline tool (http -a admin:password123 http://127.0.0.1:8000/users/)
    GET, POST, PUT, and DELETE are supported on Following Models
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
  
  Simulated Queue Job Deployment
      This simply prints the job names added to the Queue in correct executing order according to priority
      http -a admin:password123 http://127.0.0.1:8000/deploy/
