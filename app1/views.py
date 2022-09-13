from django.shortcuts import render, redirect
from app1.forms import IrisForm
import joblib
# Create your views here.

f_model = joblib.load('final_model')




def home(request):
    
    # pred = None
    
    if request.method == 'POST':
        
        form = IrisForm(request.POST)
        
        if form.is_valid():
            print('TESTING!')
            # f = form.save()
            # f.user = request.user
            # print(f.user)
            # f.save()
            
            sepal_length = form.cleaned_data.get('sepal_length')
            sepal_width = form.cleaned_data.get('sepal_width')
            petal_length = form.cleaned_data.get('petal_length')
            petal_width = form.cleaned_data.get('petal_width')
            
            pred = f_model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
            
            if pred[0] == 0:
                pred = 'pehla wala'
            elif pred[0] == 1:
                pred = 'dusra wala'
            else:
                pred = 'teesra wala'
            print(pred[0])
                
        return render(request, 'app1/display.html', {'result' : pred})
    
    else:
        form = IrisForm()
    
    return render(request, 'app1/home.html', {'form' : form})

def display(request):
    
    return render(request, 'app1/display.html')