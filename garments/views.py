from django.shortcuts import render
from garments.models import formalshirts
from garments.forms import contactform
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_list_or_404
from django.shortcuts import get_object_or_404
from garments.models import tshirt,casualshirt,jeans,sport_wear,jackets,sweater_men,tshirt_kids,shirt_kids
from garments.models import casual_pant,formal_pant,kurtas,servani,shari,Western_wear,lehgas_choli,jeans_kids
from garments.models import sport_kids

def index(request):
    westerwear1 = Western_wear.objects.all()
    casualshirt1 = casualshirt.objects.all()
    sport_kids1=sport_kids.objects.all()
    servani1=servani.objects.all()
    tshirt1=tshirt.objects.all()
    shari1=shari.objects.all()
    jackets1=jackets.objects.all()
    tshirt_kids1=tshirt_kids.objects.all()
    jeans1=jeans.objects.all()
    sport_wear1=sport_wear.objects.all()
    jeans_kids1=jeans_kids.objects.all()
    lehgas_choli1=lehgas_choli.objects.all()
    sweater_men1=sweater_men.objects.all()
    shirt_kids1=shirt_kids.objects.all()
    casual_pant1=casual_pant.objects.all()
    kurtas1=kurtas.objects.all()
    formal_pant1=formal_pant.objects.all()
    return render(request,'displayitem.html',{'westerwear': westerwear1,'westerwearname': "Women's Western wear",
                                              'casualshirt':casualshirt1,'casualshirtname':"Mens-casualshirt",
                                              'sport_kids':sport_kids1, 'sport_kidsname':"Kids sport garments",
                                              'servani':servani1,'servaniname':"Servani",
                                              'tshirt':tshirt1,'tshirtname':"Mens- tshirts",
                                              'shari':shari1,'shariname':"Womens sharis",
                                              'jackets':jackets1,'jacketsname':"Mens jackets",
                                              'tshirt_kids':tshirt_kids1,'tshirt_kidsname':"Kids Tshirts",
                                              'jeans':jeans1,'jeansname':"Mens jeans",
                                              'sport_wear':sport_wear1,'sport_wearname':"Mens Sportwear",
                                              'jeans_kids':jeans_kids1,'jeans_kidsname':"Kids wear",
                                              'lehgas_choli':lehgas_choli1,'lehgas_choliname':"Lehgas Choli",
                                               'sweater_men':sweater_men1,'sweater_menname':"Mens Sweater",
                                               'shirt_kids':shirt_kids1,'shirt_kidsname':"Kids shirt",
                                               'casual_pant':casual_pant1,'casual_pantname':"Mens casual pant",
                                               'kurtas':kurtas1,'kurtasname':"Mens kurtas",
                                               'formal_pant':formal_pant1,'formal_pantname':"Mens formal pant"})
def aboutus(request):
    return render(request,'aboutus.html')
def formal_shirts(request):
    lst=formalshirts.objects.all()
    return render(request, 'display.html', {'lst': lst, 'name': "Formal shirt"})

def thankyou(request):
    response=HttpResponse()
    response.write("<h2>Thanks for contact us<br> we just send a mail to you</h2>")
    return response
	
def contactus(request):
    form=contactform(request.POST or None)
    if form.is_valid():
        subject="this message from myGarments.com"
        message="your message:"+ request.POST.get('content')+" <br> we will get back to you soon"
        from_email=settings.EMAIL_HOST_USER
        user_email=request.POST.get('contact_email')
        to_list=[user_email,settings.EMAIL_HOST_USER]
        send_mail(subject,message,from_email,to_list,fail_silently=False)
        return HttpResponseRedirect('thankyou')
    return render(request,'contactus.html',{'form':form})
lst=[]
price=[]
def cart(request,id):
    item=get_object_or_404(formalshirts, pk=id)
    #item=formalshirts.object.get(id=id)
    lst.append(item)
    price.append(item.price)
    #str='<h1> %s'%(item)
    #return HttpResponse(str)
    return render(request, 'cart.html',{'lst':lst,'total_price':sum(price)})
def cart1(request):
    return render(request,'cart.html',{'lst':lst,'total_price':sum(price)})
def t_shirt(request):
    lst=tshirt.objects.all()
    return render(request,'display.html',{'lst':lst,'name':"Mens Tshirts"})
def casual_shirt(request):
    lst=casualshirt.objects.all()
    return render(request,'display.html',{'lst':lst,'name':"Casual shirt"})
def jeans2(request):
    lst=jeans.objects.all()
    return render(request,'display.html',{'lst':lst,'name':"Mens Jeans"})
def sport_wear1(request):
    lst=sport_wear.objects.all()
    return render(request,'display.html',{'lst':lst,'name':"Mens sportwear"})
def jacket(request):
    lst=jackets.objects.all()
    return render(request,'display.html',{'lst':lst,'name':"Mens jackets"})
def sweater(request):
    lst=sweater_men.objects.all()
    return render(request,'display.html',{'lst':lst,'name':"Mens sweater"})
def casualpant(request):
    lst=casual_pant.objects.all()
    return render(request,'display.html',{'lst':lst,'name':"Mens casual pants"})
def formalpant(request):
    lst=formal_pant.objects.all()
    return render(request,'display.html',{'lst':lst,'name':"Mens formal pants"})
def kurtas_men(request):
    lst=kurtas.objects.all()
    return render(request,'display.html',{'lst':lst,"name":'Mens kurtas'})
def servani_men(request):
    lst=servani.objects.all()
    return render(request,'display.html',{'lst':lst,'name':'Mens servani'})
def shari_women(request):
    lst=shari.objects.all()
    return render(request,'display.html',{'lst':lst,'name':'Womens shari'})
def westerwear(request):
    lst=Western_wear.objects.all()
    return render(request,'display.html',{'lst':lst,'name':"Womens western wear"})
def lehgascholi(request):
    lst=lehgas_choli.objects.all()
    return render(request,'display.html',{'lst':lst,'name':"Lehagas_Choli"})
def tshirtkids(request):
    lst=tshirt_kids.objects.all()
    return render(request,'display.html',{'lst':lst,'name':"Tshirt-Kids"})
def shirtkids(request):
    lst=shirt_kids.objects.all()
    return render(request,'display.html',{'lst':lst,'name':"shirts kids"})
def jeanskids(request):
    lst=jeans_kids.objects.all()
    return render(request,'display.html',{'lst':lst,'name':"kids-jeans"})
def sportkid(request):
    lst=sport_kids.objects.all()
    return render(request,'display.html',{'lst':lst,'name':"Kids-sport"})




# Create your views here.
