from django.shortcuts import render
import datetime
import requests
from .models import Calculate_Love
# Create your views here.

def home(request):
    try:
        if request.method=='POST':
            f = request.POST.get('fname',False)
            s = request.POST.get('sname',False)
            res = calculator(f,s)
            context ={
            'fname':res['fname'],
            'sname':res['sname'],
            'percent':int(res['percentage']),
            'result':res['result'],
            }
            return render(request,'core/result.html',context={'data':context})
        return render(request,'core/home.html')
    except:
        return render(request,'core/error.html')

def Save_In_DB(request):
    fname=request.POST['fname']
    sname=request.POST['sname']
    #ldate=datetime.datetime.today()
    st=Calculate_Love(fname=fname,sname=sname)
    st.save()
    if request.method == 'POST':
        fname = request.POST.get('fname')
        sname = request.POST.get('sname')
        if fname and sname:
            # Calculate love percentage
            love_score = hash(fname.lower() + sname.lower()) % 41 + 60
            context = {
                'love_score': love_score,
                'fname': fname,
                'sname': sname,
            }
            return render(request, 'core/Love.html', context)
    return render(request, 'core/home.html')
