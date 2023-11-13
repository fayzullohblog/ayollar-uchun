from rest_framework import generics
from .models import Course, Video, Certificate, CourseRating, CourseCompletion
from .serializer import CourseSerializer, VideoSerializer, CertificateSerializer, CourseRatingSerializer, CourseCompletionSerializer
from rest_framework import permissions, generics, status
from rest_framework.response import Response
import qrcode

class IsVideoOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsCourseOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsCourseRatingOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class CourseList(generics.ListAPIView):
    queryset = Course.objects.order_by('-created_at')
    serializer_class = CourseSerializer
    filterset_fields = ["price","average_rating"]
    search_fields = ["title","description",]
    ordering_fields = ["average_rating","price"]

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # permission_classes = [permissions.IsAuthenticated, IsVideoOwner]

    # def perform_update(self, serializer):
    #     serializer.save(owner=self.request.user)

    # def perform_destroy(self, instance):
    #     instance.delete()

class VideoList(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    ordering_fields = ["created_at"]

class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    # permission_classes = [permissions.IsAuthenticated, IsCourseOwner]

    # def perform_update(self, serializer):
    #     serializer.save(owner=self.request.user)

    # def perform_destroy(self, instance):
    #     instance.delete()

class CertificateList(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class CertificateDetail(generics.RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class CourseRatingList(generics.ListAPIView):
    queryset = CourseRating.objects.all()
    serializer_class = CourseRatingSerializer
    filterset_fields = ["rating"]

class CourseRatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseRating.objects.all()
    serializer_class = CourseRatingSerializer

    # permission_classes = [permissions.IsAuthenticated, IsCourseRatingOwner]

    # def perform_update(self, serializer):
    #     serializer.save(owner=self.request.user)

    # def perform_destroy(self, instance):
    #     instance.delete()

class CourseCompletionView(generics.ListAPIView):
    queryset = CourseCompletion.objects.all()
    serializer_class = CourseCompletionSerializer

class CourseCompletionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseCompletion.objects.all()
    serializer_class = CourseCompletionSerializer

#### CreateSertificateView


# class CreateCertificateView(generics.CreateAPIView):
#     queryset = CourseCompletion.objects.all()
#     serializer_class = CourseCompletionSerializer
#     def post(self, request, course_id):
#         user = request.user
#         course = Course.objects.get(pk=course_id)
#         completed = user.has_completed_course(course)

#         if not completed:
#             return Response({'detail': 'Course not completed.'}, status=status.HTTP_BAD_REQUEST)

#         certificate_data = {
#             'course': course,
#             'user': user,
#             'title': f"Certificate for {user.first_name} - {user.last_name}",
#         }
#         serializer = CertificateSerializer(data=certificate_data)

#         if serializer.is_valid():
#             certificate = serializer.save()

#             qr = qrcode.QRCode(
#                 version=1,
#                 error_correction=qrcode.constants.ERROR_CORRECT_L,
#                 box_size=10,
#                 border=4,
#             )
#             qr.add_data(f'http://127.0.0.1:8000/api/v1/courses/certificates/{certificate.id}/')
#             qr.make(fit=True)
#             img = qr.make_image(fill_color="black", back_color="white")

#             certificate_image = create_certificate_image(user, course, certificate, img)

#             return Response(
#                 {
#                     'certificate_image': certificate_image.url,
#                     'certificate_link': f'http://127.0.0.1:8000/api/v1/courses/certificates/{certificate.id}/',
#                 },
#                 status=status.HTTP_CREATED
#             )

#         return Response(serializer.errors, status=status.HTTP_BAD_REQUEST)
