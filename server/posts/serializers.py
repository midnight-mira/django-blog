from rest_framework import serializers
from posts.models import Posts, Images, Category

class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"

class PostSerializers(serializers.ModelSerializer):

    images = ImageSerializers(many = True, read_only = True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Posts
        fields = ["id", "author", "category", "title", "body", "images",
                  "uploaded_images"]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        post= Posts.objects.create(**validated_data)

        for image in uploaded_images:
            Images.objects.create(post = post, image =
                                  image)

        return post

