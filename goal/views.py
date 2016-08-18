from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import NameForm,DayForm
from .models import task as tk,day as dy
import re,datetime,time
from datetime import date
from datetime import datetime as dt,timedelta

def diff_dates(date1, date2):
    return abs(date2-date1).days
	
# Create your views here.
def daliy(request):
	form=DayForm
	print('daliy')
	if (1):
		try:
			dd=dy.objects.filter(date=datetime.date.today())
			print('test')
			for d in dd:
				D=d
				print('1')
			ST=dt.strptime(str(D.starttime), '%H:%M:%S')
			print(ST)
			
			print(D)
			data=[]
			print(data)
			data.append({'time':str(dt.time(ST)),'task':D.t1})
			ST=ST+ timedelta(hours=1)
			data.append({'time':str(dt.time(ST)),'task':D.t2})
			ST=ST+ timedelta(hours=1)
			data.append({'time':str(dt.time(ST)),'task':D.t3})
			ST=ST+ timedelta(hours=1)
			data.append({'time':str(dt.time(ST)),'task':D.t4})
			ST=ST+ timedelta(hours=1)
			data.append({'time':str(dt.time(ST)),'task':D.t5})
			ST=ST+ timedelta(hours=1)
			data.append({'time':str(dt.time(ST)),'task':D.t6})
			ST=ST+ timedelta(hours=1)
			data.append({'time':str(dt.time(ST)),'task':D.t7})
			ST=ST+ timedelta(hours=1)
			data.append({'time':str(dt.time(ST)),'task':D.t8})
			ST=ST+ timedelta(hours=1)
			data.append({'time':str(dt.time(ST)),'task':D.t9})
			ST=ST+ timedelta(hours=1)
			data.append({'time':str(dt.time(ST)),'task':D.t10})
			ST=ST+ timedelta(hours=1)
			data.append({'time':str(dt.time(ST)),'task':D.t11})
			ST=ST+ timedelta(hours=1)
			data.append({'time':str(dt.time(ST)),'task':D.t12})
			ST=ST+ timedelta(hours=1)
			data.append({'time':str(dt.time(ST)),'task':D.t13})
			ST=ST+ timedelta(hours=1)
			data.append({'time':str(dt.time(ST)),'task':D.t14})
			ST=ST+ timedelta(hours=1)
			data.append({'time':str(dt.time(ST)),'task':D.t15})
			ST=ST+ timedelta(hours=1)
			data.append({'time':str(dt.time(ST)),'task':D.t16})
			print(data)
			localtime   = time.localtime()
			timeString  = time.strftime("%H:%M:%S", localtime)
			print(D.starttime,timeString)
			diff=dt.strptime(timeString, '%H:%M:%S')-dt.strptime(str(D.starttime), '%H:%M:%S')
			di=int((diff.seconds)/3600)
			print(data[di]['task'])
			print(diff.seconds,(3600-(diff.seconds)%3600)*1000,di)
			return render(request,'goal/daliy.html',{'data':data,'nxtt':(3600-(diff.seconds)%3600)*1000,'nxttk':data[di]['task']})
		except:
			print('except')
			tsl=tk.objects.exclude(next='NoNext').filter(previous='NoPrevious')
			ts=tk.objects.all()
			T=[]
			for d in ts:
				if ((d.progressvalue>99) and (d.next!='NoNext')):
					if(tk.objects.filter(next=d.next).exclude(progressvalue__lte=100)):
						tmp=tk.objects.filter(next=d.next).exclude(progressvalue__lte=100)
						for ttmp in tmp:
							T.append(ttmp.text)
					print('>99')
					print(T)
				if ((d.progressvalue<100) and (d.previous=='NoPrevious') and (d.topbranch!='Firsttask')):
					T.append(d.text)
					print('<100')
					print(T)
			
			return render(request,'goal/daliy.html',{'form':form,'task':T})
def minitask(request):
	return render(request,'goal/minitask.html')
			
def deltoday(request):
	try:
		dd=dy.objects.filter(date=datetime.date.today())
		dd.delete()
		return HttpResponseRedirect(reverse('goal:task'))
	except:
		print('no task yday')
		return HttpResponseRedirect(reverse('goal:task'))
def task(request):
	form=NameForm
	if (1):
		try:
			t=get_list_or_404(tk)
			print('try')
		except:
			print('except')
			return render(request,'goal/task.html',{'form':form})
		else:
			co=1
			for tt in t:
				if(datetime.date.today()>tt.startdate):
					pv=float(diff_dates(datetime.date.today(),tt.startdate))/float(diff_dates(tt.completedate,tt.startdate))
					val=tk.objects.get(text=tt.text)
					val.progressvalue=(pv*100)
				else:
					val=tk.objects.get(text=tt.text)
					val.progressvalue=0
				val.save()
			t=get_list_or_404(tk)
			T=[]
			name=[]
			id=[]
			iddic={}
			i=0
			for tt in t:
				if tt.topbranch not in name:
					name.append(tt.topbranch)
					id.append('id'+str(i))
					i+=1
				if tt.text not in name:
					name.append(tt.text)
					id.append('id'+str(i))
					i+=1
				if tt.next not in name:
					name.append(tt.next)
					id.append('id'+str(i))
					i+=1
				if tt.previous not in name:
					name.append(tt.previous)
					id.append('id'+str(i))
					i+=1
			for tt in range(len(id)):
				iddic[name[tt]]=id[tt]
			for tt in t:
				T.append({'text':tt.text,'topbranch':tt.topbranch,
				'next':tt.next,'previous':tt.previous,
				'startdate':(tt.startdate).isoformat(),'completedate':(tt.completedate).isoformat(),
				'progressvalue':tt.progressvalue,'audio':tt.audio,
				'txtid':iddic[tt.text],'tbid':iddic[tt.topbranch],'nxtid':iddic[tt.next],
				'preid':iddic[tt.previous]})
			print(T)	
			for t in range(len(T)):
				if T[t]['text']=='Get more  friends':
					T[t]['progressvalue']=90
			return render(request,'goal/task.html',{'form':form,'co':co,'t':T})
def newdaliy(request):
	if request.method=="POST":
		form=DayForm(request.POST)
		print('test')
		print(form.errors)
		if form.is_valid():
			print('test')
			ST=form.cleaned_data['starttime']
			T1=form.cleaned_data['t1']
			T2=form.cleaned_data['t2']
			T3=form.cleaned_data['t3']
			T4=form.cleaned_data['t4']
			T5=form.cleaned_data['t5']
			T6=form.cleaned_data['t6']
			T7=form.cleaned_data['t7']
			T8=form.cleaned_data['t8']
			T9=form.cleaned_data['t9']
			T10=form.cleaned_data['t10']
			T11=form.cleaned_data['t11']
			T12=form.cleaned_data['t12']
			T13=form.cleaned_data['t13']
			T14=form.cleaned_data['t14']
			T15=form.cleaned_data['t15']
			T16=form.cleaned_data['t16']
			print(ST,T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16)
			d=dy(starttime=ST,t1=T1,t2=T2,t3=T3,t4=T4,t5=T5,t6=T6,t7=T7,t8=T8,t9=T9,t10=T10,t11=T11,t12=T12,t13=T13,t14=T14,t15=T15,t16=T16)
			d.save()
			return HttpResponseRedirect(reverse('goal:daliy'))
def newtask(request):
	print('test')
	if request.method=="POST":
		form=NameForm(request.POST)
		print(form.errors)
		if form.is_valid():
			txt=form.cleaned_data['text']
			tb=form.cleaned_data['topbranch']
			nxt=form.cleaned_data['next']
			pre=form.cleaned_data['previous']
			sdte=form.cleaned_data['startdate']
			cdte=form.cleaned_data['completedate']
			pv=form.cleaned_data['progressvalue']
			au=form.cleaned_data['audio']
			au='goal/media'+au.replace('\\','/')
			try:
				t=tk.objects.get(text=txt)
				t.delete()
				try:
					t=tk.objects.get(text=pre)
					t.next=txt
					t.save()
					t=tk.objects.get(previous=pre)
					print('found',pre)
					t.previous=txt
					t.save()
					t=tk(text=txt,topbranch=tb,next=nxt,previous=pre,progressvalue=pv,startdate=sdte,completedate=cdte,audio=au)
					t.save()
				except:
					print('not found')
					t=tk(text=txt,topbranch=tb,next=nxt,previous=pre,progressvalue=pv,startdate=sdte,completedate=cdte,audio=au)
					t.save()
			except:
				try:
					t=tk.objects.get(text=pre)
					t.next=txt
					t.save()
					t=tk.objects.get(previous=pre)
					print('found',pre)
					t.previous=txt
					t.save()
					t=tk(text=txt,topbranch=tb,next=nxt,previous=pre,progressvalue=pv,startdate=sdte,completedate=cdte,audio=au)
					t.save()
				except:
					print('not found')
					t=tk(text=txt,topbranch=tb,next=nxt,previous=pre,progressvalue=pv,startdate=sdte,completedate=cdte,audio=au)
					t.save()
			
			print('ok')
			return HttpResponseRedirect(reverse('goal:task'))
		else:
			print('not ok')