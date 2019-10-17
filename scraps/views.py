from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import csv
import re
from .forms import RequestForm


def datafilter(soup):
    linklist = []
    for links in soup.find_all('a'):
        link = links.get('href')
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', link)
        if(url):
            linklist.append(url[0])
    p_tag_list = []
    for p_tag in soup.find_all('p'):
        p_tag_list.append(p_tag.text)
        
    data = {
        "title": soup.title.name,
        "links": linklist,
        "paragraph": p_tag_list
    }

    f = open("sample.csv", "w")
    writer = csv.DictWriter(
        f, fieldnames=["fruit", "count"])
    writer.writeheader()
    writer.writerow({"fruit": "apple", "count": "1"})
    writer.writerow({"fruit": "banana", "count": "2"})
    f.close()
    return data

    

def home(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            res = requests.get(url)
            soup = BeautifulSoup(res.text, 'html.parser')
            response = datafilter(soup)
            return render_to_response('datalist.html', {'item_list': response})

    else:
        form = RequestForm()
    return render(request, 'home.html', {'form': form})
