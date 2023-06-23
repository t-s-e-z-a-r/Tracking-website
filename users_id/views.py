from django.shortcuts import render
from Component.settings import CHANNEL_LAYERS
from . models import User_Url, Url
import uuid
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your views here.

def home_view(request):
    if request.META['SERVER_PORT'] == '8080':
        return render(request, 'admin.html')
    else:
        end_user_id = request.COOKIES.get('end_user_id')
        if not end_user_id:
            end_user_id = generate_end_user_id()
        web_page_url = '/'
        response = render(request, 'home.html')
        response.set_cookie('end_user_id', end_user_id)
        save_information(end_user_id, web_page_url)
        return response


def id_view(request, pk):
    return render(request, 'admin_id.html', {'pk': pk})

    
def page1_view(request):
    end_user_id = request.COOKIES.get('end_user_id')
    web_page_url = '/page1/'
    save_information(end_user_id, web_page_url)
    return render(request, 'page1.html')


def page2_view(request):
    end_user_id = request.COOKIES.get('end_user_id')
    web_page_url = '/page2/'
    save_information(end_user_id, web_page_url)
    return render(request, 'page2.html')


def create_user_cookie(id):
    user = User_Url(ID_User=id)
    user.save()
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
    'global1',
    {
        'type': 'update1',
        'message': "New request"
    }
    )

def save_information(id, url):
    channel_layer = get_channel_layer()
    try:
        user = User_Url.objects.get(ID_User=id)
        url_obj = Url(user=user, Url_User=url)
        url_obj.save()
    except :
        create_user_cookie(id)
        user = User_Url.objects.get(ID_User=id)
        url_obj = Url(user=user, Url_User=url)
        url_obj.save()
    finally:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
        'global2',
        {
            'type': 'send_request',
            'message': "New request"
        }
        )


def generate_end_user_id():
    end_user_id = str(uuid.uuid4())
    return end_user_id