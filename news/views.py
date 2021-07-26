from django.shortcuts import render
from .models import New
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def addnew(rq):
	cnt=len(New.objects.filter(new_title=rq.GET['title']))
	if cnt>0:
		return HttpResponse('Новость уже есть в базе!')
	n=New()
	n.new_title=rq.GET['title']
	n.new_url=rq.GET['url']
	n.new_date=datetime.fromisoformat(rq.GET['date'])
	n.save()
	#return render(rq,'Новость добавлена!')
	#print('Новость добавлена!')
	return HttpResponse('Новость добавлена! ')

def shownews(rq):
	w=rq.GET.get('with', None)
	t=rq.GET.get('to', None)
	if w and t:
		#ns=New.objects.filter(new_date=(datetime.fromisoformat(w),datetime.fromisoformat(t)))
		w=datetime.fromisoformat(w)
		t=datetime.fromisoformat(t)
		ns=New.objects.filter(new_date__range=(w,t))
		w=w.isoformat()
		t=t.isoformat()
	else:
		ns=New.objects
	return render(rq,'news/news.html',{'news':ns,'with':w,'to':t})


