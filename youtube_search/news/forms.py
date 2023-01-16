from .models import ChannelAdd
from django.forms import ModelForm, TextInput, Textarea


class ChannelAddForm(ModelForm):
    class Meta:
        model = ChannelAdd
        fields = ['channel_url', 'channel_name', 'channel_desc']

        widgets = {
            'channel_url': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес канала'
            }),
            'channel_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название канала'
            }),
            'channel_desc': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание канала'
            }),
        }
