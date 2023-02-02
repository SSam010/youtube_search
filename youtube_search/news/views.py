from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, UpdateView, DeleteView
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from slugify import slugify

from .Serializers import NewsSerializer
from .forms import ChannelAddForm
from .models import Channel, ChannelAdd
from .permissions import *
from .scripts.news import plot_venna, plot_boxplot, plot_timeline


# Create your views here.

@cache_page(60 * 30)
def news_home(request):
    channel = Channel.objects.order_by('channel_name')
    plot_venna.create_venna()
    plot_boxplot.create_boxplot()
    plot_timeline.create_timeline()
    return render(request, 'news/news_home.html', {'channel': channel})


class NewsUpdateView(UpdateView):
    model = ChannelAdd
    template_name = 'news/news-update.html'
    form_class = ChannelAddForm


class NewsDetailView(DetailView):
    model = Channel
    template_name = 'news/details_view.html'
    context_object_name = 'Channel'


class NewsDeleteView(DeleteView):
    model = ChannelAdd
    template_name = 'news/news-delete.html'
    success_url = '/news/create'


def create(request):
    error = ''
    if request.method == "POST":
        form = ChannelAddForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.slug = slugify(form.channel_name)
            form.save()
        else:
            error = "Форма заполнена некорректно"
        return

    form = ChannelAddForm()
    channel_add = ChannelAdd.objects.order_by('time_create').select_related('user')
    data = {'form': form,
            'error': error,
            'channel_add': channel_add}
    return render(request, 'news/create.html', data)


class ApiNewsCreate(generics.ListCreateAPIView):
    queryset = ChannelAdd.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class ApiNewsUpdate(generics.RetrieveUpdateAPIView):
    queryset = ChannelAdd.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (OwnerAndStaffOrReadOnly,)
    lookup_field = 'slug'


class ApiNewsDelete(generics.RetrieveDestroyAPIView):
    queryset = ChannelAdd.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (OwnerAndStaffOrReadOnly,)
    lookup_field = 'slug'
