from django.conf.urls import url

from anup.views import ChartData, HomeView, get_data
from  . import views

from django.conf import settings
from django.views.static import serve




urlpatterns =[
    #url(r'^$', views.index),
    # url(r'^signup$', views.signup, name='signup'),
    #url(r'^/anup',views.UserFormView.as_view, name='Userform'),
    #url(r'^signup/$',views.signup , name='signup'),
    #url(r'^register/', views.post_new, name='post_new'),
    url(r'^login/',views.index,name="index"),
    url(r'^role/',views.role,name="role"),
    url(r'^display/search/',views.search,name='search'),
    url(r'^register/',views.create_user, name='create_user'),
    url(r'^display/',views.display, name='display'),
    url(r'anup/(?P<pk>[\w\-]+)/edit/$',views.edit_post, name="edit_post"),
    #url(r'anup/(?P<pk>[\w\-]+)/login/$',views.rolelogin, name="rolelogin"),
    url(r'anup/(?P<pk>[\w\-]+)/delete/$', views.delete_post, name="delete_post"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'anup/(?P<pk>[\w\-]+)/validate/$', views.validate, name="validate"),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^activate1/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate1, name='activate1'),
    #url(r'search_connections/(?P<data>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.rolelogin,name="rolelogin"),
    url(r'selectemail/',views.selectemail, name="selectemail"),
    url(r'select/',views.select, name="select"),
    url(r'^activate2/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate2, name='activate2'),
    #url(r'anup/(?P<pk>[\w\-]+)/login/$',views.rolelogin, name="rolelogin"),
    url(r'admin/interface/',views.admininterface,name="admininterface"),
    url(r'profile/',views.profile, name="profile"),
    url(r'photo/',views.adds,name="adds"),
    url(r'permission/',views.permission,name="permission"),
    url(r'adminhome/',views.adminhome,name="adminhome"),
    url(r'addrole/', views.addrole, name="addrole"),
    url(r'userright/', views.userright, name="userright"),
    url(r'anup/(?P<pk>[\w\-]+)/active/$', views.active, name="active"),
    url(r'anup/(?P<pk>[\w\-]+)/inactive/$', views.inactive, name="inactive"),
    url(r'^api/data/$',views.get_data, name="get_data"),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'work/',views.work,name="work")
    #url(r'anup/(?P<pk>[\w\-]+)/login/$', views.admininterface, name="rolelogin"),

    #url(r'search/$',views.search,name="search"),
     #url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),

]


