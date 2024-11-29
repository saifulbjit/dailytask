from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializer import JobSerializer
from .permission import IsAdminOrReadOnly
from jobs.models import Job, Application, Category


class JobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)



class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    permission_classes = [IsAdminOrReadOnly]