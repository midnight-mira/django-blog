from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from posts.models import Posts
from posts.serializers import PostSerializers

class PostCreateView(CreateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = PostSerializers
    
