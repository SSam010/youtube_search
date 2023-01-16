from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .models import Channel, ChannelAdd
from .forms import ChannelAddForm
from .scripts.news import plot_venna, plot_boxplot, plot_timeline


# Create your views here.

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
        form = ChannelAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
        else:
            error = "Форма заполнена некорректно"

    form = ChannelAddForm()
    channel_add = ChannelAdd.objects.order_by('channel_name')
    data = {'form': form,
            'error': error,
            'channel_add': channel_add}
    return render(request, 'news/create.html', data)
