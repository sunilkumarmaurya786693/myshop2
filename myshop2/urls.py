"""myshop2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from garments.views import index,aboutus,formal_shirts,contactus,thankyou,cart,cart1,t_shirt,servani_men,shari_women
from garments.views import casual_shirt,jeans2,sport_wear1,jacket,sweater,casualpant,formalpant,kurtas_men,westerwear
from garments.views import lehgascholi,tshirtkids,shirtkids,jeanskids,sportkid


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$',index,name='index'),
	#url(r'^index',index,name='index'),
	url(r'^aboutus$',aboutus),
	url(r'^formal_shirts$',formal_shirts),
	url(r'^contactus$', contactus),
	url(r'^thankyou$',thankyou),
    url(r'^cart(\d{1,2})$',cart),
	url(r'^cart1$',cart1),
	url(r'^t_shirt$',t_shirt),
	url(r'casual_shirt$',casual_shirt),
	url(r'^jeans1$',jeans2),
	url(r'^sport_wear$',sport_wear1),
	url(r'^jackets$',jacket),
	url(r'^sweater_men$',sweater),
	url(r'^casual_pant$',casualpant),
	url(r'^formal_pant$',formalpant),
	url(r'^kurtas$',kurtas_men),
	url(r'^servani$',servani_men),
	url(r'^shari$',shari_women),
	url(r'^Wester_wear$',westerwear),
	url(r'^lehagascholi$',lehgascholi),
	url(r'^tshirtkids',tshirtkids),
	url(r'^shirtkid$',shirtkids),
	url(r'^kidsjeans$',jeanskids),
	url(r'^sport_kid$',sportkid),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
