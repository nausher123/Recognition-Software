from genericpath import exists
from multiprocessing.forkserver import write_signed
from pickletools import read_string1
from turtle import write_docstringdict
from django.shortcuts import render
from django.http import HttpResponse
from .models import ThresholdData1, ThresholdData_O, Sat_Curves
from .forms import ThresholdForm1, SatForm





def alevel(request):
    out_data= {
        'grade': "", 
        'form': ThresholdForm1,
        'A': "",
        'B': "",
        'C': "",
        'D': "",
        'E': "",
        "U": "",
        "exist": True,
        "search_string": "",

        }

    
    
        
        


    if request.method== "POST":
        form= ThresholdForm1(request.POST)
        if form.is_valid():
            subject= form.cleaned_data['subject']
            variant= str(form.cleaned_data['variant'])
            month= form.cleaned_data['month']
            year= str(form.cleaned_data['year'])
            marks= form.cleaned_data['marks']
            year1= year[2:4]
            subject= subject.lower()
            if subject=="math":
                s_code= "9709"
            elif subject=="physics":
                s_code= "9702"
            
            search_string= f"{s_code}/{variant}/{month}/{year1}"
            

            if ThresholdData1.objects.filter(searchID=search_string).exists() and marks is None:
                out_data['search_string']= search_string
                data= ThresholdData1.objects.get(searchID=search_string)
                
            
            

                out_data['A']= data.a
                out_data['B']= data.b
                out_data['C']= data.c
                out_data['D']= data.d
                out_data['E']= data.e

                return render(request, 'alevel.html', out_data)
            
            elif ThresholdData1.objects.filter(searchID=search_string).exists():
                data= ThresholdData1.objects.get(searchID=search_string)
                
            
            

                out_data['A']= data.a
                out_data['B']= data.b
                out_data['C']= data.c
                out_data['D']= data.d
                out_data['E']= data.e
                    

                    




                if marks>=data.a:
                    out_data['grade']="A"
                elif marks>=data.b:
                    out_data["grade"]= "B"
                elif marks>=data.c:
                    out_data["grade"]= "C"
                elif marks>=data.d:
                    out_data["grade"]= "D"
                elif marks>=data.e:
                    out_data["grade"]= "E"
                else:
                    out_data['grade']="U"



                return render(request, 'alevel.html',out_data)
            else:
                out_data["exist"]= False
                return render(request, 'alevel.html', out_data )
            
                
                
            

    return render(request, 'alevel.html', {'form': ThresholdForm1})
        





    










def olevel(request):
    out_data= {
        'grade': "", 
        'something': "",
        'form': ThresholdForm1,
        'A': "",
        'B': "",
        'C': "",
        'D': "",
        'E': "",
        "U": "",
        'exist': True,
        'search_string': "",

        }

    
    if request.method=="POST":
        form= ThresholdForm1(request.POST)
        if form.is_valid():
            subject= form.cleaned_data['subject']
            variant= str(form.cleaned_data['variant'])
            month= form.cleaned_data['month']
            year= str(form.cleaned_data['year'])
            marks= form.cleaned_data['marks']
           
            year1= year[2:4]
            subject= subject.lower()
            if subject=="math":
                s_code= "4024"
            elif subject=="physics":
                s_code= "5054"
            
            search_string= f"{s_code}/{variant}/{month}/{year1}"
            

            if  ThresholdData_O.objects.filter(searchID= search_string).exists() and marks is None:
                out_data['search_string']= search_string
                data= ThresholdData_O.objects.get(searchID=search_string)


                

                out_data['A']= data.a
                out_data['B']= data.b
                out_data['C']= data.c
                out_data['D']= data.d
                out_data['E']= data.e
                return render(request, 'olevel.html', out_data)
            elif ThresholdData_O.objects.filter(searchID= search_string).exists():
            
                data= ThresholdData_O.objects.get(searchID=search_string)


                

                out_data['A']= data.a
                out_data['B']= data.b
                out_data['C']= data.c
                out_data['D']= data.d
                out_data['E']= data.e
                    

                



                if marks>=data.a:
                    out_data['grade']="A" 
                elif marks>=data.b:
                    out_data["grade"]= "B"
                elif marks>=data.c:
                    out_data["grade"]= "C"
                elif marks>=data.d:
                    out_data["grade"]= "D"
                elif marks>=data.e:
                    out_data["grade"]= "E"
                else:
                    out_data['grade']="U"
                return render(request, 'olevel.html', out_data)


                    
        


            else:
                out_data['exist']= False
                
            return render(request, 'olevel.html', out_data)






       
        
        
        

    return render(request, 'olevel.html', {'form': ThresholdForm1})
    

#home
def home(request):
    return render(request, 'home.html')









#sat
def sat(request):
    out={
        'math': 0,
        'reading': 0,
        'writing': 0,
        'form': SatForm,
        'total': 0,
        
        }
    if request.method== 'POST':
        form= SatForm(request.POST)
        if form.is_valid():
    
            testno= form.cleaned_data['practice_test']
            raw_score_math= form.cleaned_data['incorrect_in_math']
            raw_score_reading= form.cleaned_data['incorrect_in_reading']
            raw_score_writing= form.cleaned_data['incorrect_in_writing']
            


            if raw_score_reading is None and raw_score_writing is None:
                raw_score_math= str(58-raw_score_math)
                s_string_m= f"{testno}/{raw_score_math}"
                data_m = Sat_Curves.objects.get(s_id= s_string_m)
                out['math']= data_m.points_math
                out['total']= out['math']
            elif raw_score_reading is None and raw_score_math is None:
                raw_score_writing= str((44-form.cleaned_data['incorrect_in_writing']))
                s_string_w= f"{testno}/{raw_score_writing}"
                data_w= Sat_Curves.objects.get(s_id= s_string_w)
                out['writing']= data_w.points_write*10
                out['total']= out['writing']

            elif raw_score_math is None and raw_score_writing is None: 
                raw_score_reading= str(52-raw_score_reading)
                s_string_r= f"{testno}/{raw_score_reading}"
                data_r= Sat_Curves.objects.get(s_id= s_string_r)
                out['reading']= data_r.points_read*10
                out['total']= out['reading']


            elif raw_score_math is None:
                raw_score_reading= str((52-form.cleaned_data['incorrect_in_reading']))
                raw_score_writing= str((44-form.cleaned_data['incorrect_in_writing']))
                
                s_string_r= f"{testno}/{raw_score_reading}"
                s_string_w= f"{testno}/{raw_score_writing}"

                


                
                data_w= Sat_Curves.objects.get(s_id= s_string_w)
                data_r= Sat_Curves.objects.get(s_id= s_string_r)

            

                out['reading']= data_r.points_read*10
                out['writing']= data_w.points_write*10
                out['total']= out['reading']+ out['writing']  
            elif raw_score_reading is None:
                raw_score_writing= str((44-form.cleaned_data['incorrect_in_writing']))
                s_string_w= f"{testno}/{raw_score_writing}"
                data_w= Sat_Curves.objects.get(s_id= s_string_w)
                out['writing']= data_w.points_write*10
                raw_score_math= str(58-raw_score_math)
                s_string_m= f"{testno}/{raw_score_math}"
                data_m = Sat_Curves.objects.get(s_id= s_string_m)
                out['math']= data_m.points_math




                out['total']= out['writing']+ out['math'] 
            elif raw_score_writing is None:
                raw_score_math= str(58-raw_score_math)
                s_string_m= f"{testno}/{raw_score_math}"
                data_m = Sat_Curves.objects.get(s_id= s_string_m)
                out['math']= data_m.points_math

                raw_score_reading= str(52-raw_score_reading)
                s_string_r= f"{testno}/{raw_score_reading}"
                data_r= Sat_Curves.objects.get(s_id= s_string_r)
                out['reading']= data_r.points_read*10
                out['total']= out['reading'] + out['math']
            else:
                raw_score_math= str(58-raw_score_math)
                s_string_m= f"{testno}/{raw_score_math}"
                data_m = Sat_Curves.objects.get(s_id= s_string_m)
                out['math']= data_m.points_math

                raw_score_reading= str(52-raw_score_reading)
                s_string_r= f"{testno}/{raw_score_reading}"
                data_r= Sat_Curves.objects.get(s_id= s_string_r)
                out['reading']= data_r.points_read*10

                raw_score_writing= str((44-form.cleaned_data['incorrect_in_writing']))
                s_string_w= f"{testno}/{raw_score_writing}"
                data_w= Sat_Curves.objects.get(s_id= s_string_w)
                out['writing']= data_w.points_write*10
                out['total']= out['writing']+ out['math'] + out['reading']
                


            


        return render(request, 'sat.html', out)



    form= SatForm

    return render(request, "sat.html", out)






