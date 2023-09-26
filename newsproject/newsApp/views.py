from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    country = request.GET.get('country')
    category=request.GET.get('category')

    if country:
        url= f'https://newsapi.org/v2/top-headlines?country={country}&apiKey=e25d540430c14de981cff8d51d96613f'

        response=requests.get(url)
        data=response.json()
        articles=data['articles']
    else:
        url= f'https://newsapi.org/v2/top-headlines?category={category}&apiKey=e25d540430c14de981cff8d51d96613f'

        response=requests.get(url)
        data=response.json()
        articles=data['articles']

    
    
    
    context={
        'articles':articles
    }
    return render(request,'index.html',context)
