#from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Board

# Create your views here.

from .models import Board


def index(request):
    board_list = Board.objects.order_by('-create_date')
    context = {'board_list': board_list} #딕셔너리형 
    return render(request, 'board/board_list.html', context)

def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board': board}
    return render(request, 'board/board_detail.html', context)

class create(generic.CreateView):
    model = Board
    fields = ['subject', 'content', 'create_date']
    success_url = reverse_lazy('board:list')
    template_name_suffix = '_create'