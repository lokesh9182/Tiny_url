from django.shortcuts import render
from urlapp import models,code
from django.http import HttpResponseRedirect 

# urltable.objects.filter(classroom=1)).only('fistname','age')

def originalpage(request,id):
    # print("--------------iddd----: ",id)
    dd=models.urltable.objects.filter(shorturl=id)
    return HttpResponseRedirect(dd[0].longurl)

# http://localhost:8000/url/

def homepage(request):
    if request.method=="POST":
        l_url=request.POST.get('url')
        database=models.urltable.objects.all()

        if(models.urltable.objects.count()==0):
            shorturlint=1
        else:
            x=models.urltable.objects.count()
            shorturlint=database[x-1].slno + 1
        s_url=code.g_shorturl(shorturlint)

        ins=models.urltable(slno=shorturlint, longurl=l_url, shorturl=s_url)
        ins.save()
        return render(request,'nw.html',{"link":"http://localhost:8000/url/"+s_url })
        
    return render(request,'main.html')