from rest_framework import serializers
from slugify import slugify

from .models import ChannelAdd


class NewsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    slug = serializers.ReadOnlyField()

    class Meta:
        model = ChannelAdd
        fields = ("channel_url", "channel_name", "channel_desc", "time_create", "time_update", "user", "slug")

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['slug'] = slugify(attrs['channel_name'])
        return attrs
