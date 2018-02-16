from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.files.storage import  FileSystemStorage
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import UpdateView, DeleteView
from rest_framework.response import Response
from rest_framework.views import APIView

from anup import models
from anup.form import UserForm
from anup.tokens import account_activation_token
from .models import User, admin1, Role, Profile, Article, right
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.template.loader import render_to_string
#from anup.views import APIView
#from rest_framework.response import Response



def index(request):
    # print(request);
    # if request.is_ajax():
    if request.method == 'POST':
        # username="admin"
        # password="admin"

        # return HttpResponse(request.POST.get('username'))

        username = request.POST.get('username')
        # return HttpResponse(username)
        password = request.POST.get('password')
        # return HttpResponse(password)
        # username = self.cleaned_data['username']
        # password=self.cleaned_data['password']
        if admin1.objects.filter(username=username, password=password).exists():
            # i#f username==admin1.username and password==admin1.password:
            # if user:
            # return HttpResponse("koijiopjuioj")
            # login(request,admin1)
            # else:
            # return render(request, 'anup/user_list.html')
            return render_to_response('anup/table.html', {'query_results': models.User.objects.all()})

        else:
            # User=authenticate(username=username,password=password)
            # if user is not None:

            # return HttpResponse("not valid")
            # login(request,User)
            return render_to_response('anup/user_list.html')
            # return render_to_response('anup/table.html', {'query_results': models.User.objects.all()})

    return render(request, 'anup/login1.html')

    # form1 = UserForm
    # Eform = form1.UserForm
    # return render(request, "anup/login1.html")

    # return HttpResponse("<h1>Hello your page is awsome</h1>")


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):

        if account_activation_token.check_token(User, token):
            # user.is_active = True
            # user.save()
            # login(request, User)
            # return redirect('home')
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')


def post_new(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        # return HttpResponse(request.get('first_name'))

        if form.is_valid():
            user = form.save(commit=False)

            # User.first_name=form.cleaned_data.get('first_name')
            # User.last_name=form.cleaned_data.get('last_name')

            # User.email=form.cleaned_data.get('email')
            # User.birth_date=form.cleaned_data.get('Dob')

            # User.country=form.cleaned_data.get('country')


            user.is_active = False
            # form=User(First_name=first_name,last_name=last_name,email=email,birth_date=birth_date,country=country)
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('anup/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # user.email(subject, message)
            # mail_subject = 'Activate your blog account.'
            # to_email = form.cleaned_data.get('email')
            email1 = EmailMessage(subject, message, to=[user.email])
            email1.send()
            # return redirect('account_activation_sent')
            return HttpResponse('<h1>Please Check your Email for verfication</h1>')


    else:
        form = UserForm()
    return render(request, 'anup/login.html', {'form': form})
    # return HttpResponse("rfgdrfdgtrfy")


# def my_view(request):
# query_results=User.objects.all()


# for my_obj in query_results:
# $   my_obj.user = uDict.get(my_obj.C)
# context=query_results
# return render(request,'anup/table.html')

def display(request):
    return render_to_response('anup/table.html', {'query_results': models.User.objects.all()})


class UserUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'birth_date', 'address']
    template_name_suffix = 'anup/ update_form'


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('anup:index')


def edit_post(request, pk):
    instance1 = get_object_or_404(User, pk=pk)
    # User.objects.get(pk=pk)
    if request.method == 'POST':

        form = UserForm(request.POST, instance=instance1)

        # return HttpResponse(request.get('first_name'))

        if form.is_valid():
            instance1 = form.save(commit=False)
            # instance1.first_name=request.user
            # User.first_name=request.first_nmae
            # User.last_name=request.last_name
            # User.email=request.email
            # User.birth_date=request.birth_date
            # User.address=request.address
            instance1.save()
            # return redirect('anup:index')
            return HttpResponse('<h1>You have registered successfully</h1>')
    else:
        form = UserForm(instance=instance1)
    return render(request, 'anup/login.html', {'form': form})


def delete_post(request, pk):
    instance2 = get_object_or_404(User, pk=pk)
    # if request.method=='POST':
    # form=UserForm(request.POST,instance=instance2)
    # if form.is_valid():
    # instance2=form.save(commit=False)
    instance2.delete()
    messages.success(request, "successfully delete")
    return redirect('anup/table.html')
    # else:
    # form=UserForm()
    # return  HttpResponse("<h1>you have delete it<h1>")


def validate(request, pk):
    instance1 = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=instance1)
        if form.is_valid():
            instance1 = form.save(commit=False)
            # prnt = User.objects.get(id=pk)
            # instance1.request_status = 1
            # instance1.user.is_active = True
            # instance1.user.save()
            instance1.save()
            # instance1.save()
            return HttpResponse('<h1>**********</h1>')
    else:
        form = UserForm(instance=instance1)
    return render(request, 'anup/abc.html', {'form': form})


def search(request):
    user = None
    if request.method == 'GET':
        search = request.GET.get('search')
        if search:
            # query_list=User.objects.filter(first_name_contains=search)
            # query_list=User.objects.filter(query_icontains=query1)
            # return HttpResponse("<h1>Hello you have searched</h1>")

            # try:
            # user=User.objects.raw('select * from table where address=%s',tuple([address]))
            user = User.objects.filter(
                Q(first_name__contains=search) | Q(last_name__contains=search) | Q(email__contains=search) | Q(
                    address__contains=search) | Q(birth_date__contains=search))
            # user=User.objects.all()
            # Q(last_name__contains=search) |
            # Q(email__contains=search) |
            # Q(birth_date__contains=search) |
            # Q(address__contains=search))
            # return HttpResponse(user)
            # html = render_to_string('sea.html',{'user':user})
            return render(request, 'anup/rolesearch.html', {'user': user})
            # data_json = json.loads(json.dumps(user))
            # return HttpResponse(data_json)
            # html = render_to_string('search_results.html',{'user':user})
            # query_list.save()
            # except:
            # pass

    return render(request, 'anup/AddRole.html', {'user': user})
    # return redirect('anup/table.html')


def create_user(request):
    if request.method == 'POST':
        # User.save(commit=False)
        username = request.POST['username']
        # password=request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        birth_date = request.POST['birth_date']
        address = request.POST['address']

        User.objects.create(
            username=username,
            # password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            birth_date=birth_date,
            address=address,
        )

        current_site = get_current_site(request)
        subject = 'Activate Your MySite Account'
        message = render_to_string('anup/account_activation_email.html', {
            'user': User,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(User.pk)),
            'token': account_activation_token.make_token(User),
        })
        # user.email(subject, message)
        # mail_subject = 'Activate your blog account.'
        # to_email = form.cleaned_data.get('email')
        email1 = EmailMessage(subject, message, to=[User.email])
        email1.send()
        # return redirect('account_activation_sent')
        return HttpResponse('<h1>Please Check your Email for verfication</h1>')
        # return render(request,'anup/login1.html',{'User':User})

    return render(request, 'anup/register.html', {'user': User})


def role(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        role = request.POST['role']

        Role.objects.create(
            username=username,
            first_name=first_name,
            email=email,
            role=role,
        )
        current_site = get_current_site(request)
        subject = 'Activate Your MySite Account'
        message = render_to_string('anup/roleactivate.html', {
            'role': Role,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(Role.pk)),
            'token': account_activation_token.make_token(Role),
        })
        # user.email(subject, message)
        # mail_subject = 'Activate your blog account.'
        # to_email = form.cleaned_data.get('email')
        email1 = EmailMessage(subject, message, to=[Role.email])
        email1.send()
        # return redirect('account_activation_sent')
        return HttpResponse('<h1>Please Check your Email for verfication</h1>')

    return render(request, 'anup/role.html', {'role': Role})


def activate1(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        Role.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Role.DoesNotExist):

        if account_activation_token.check_token(Role, token):
            # user.is_active = True
            # user.save()
            # login(request, User)
            # return redirect('home')
            return HttpResponse("kindly love me ")

        else:
            return HttpResponse('Activation link is invalid!')





def selectemail(request):
    # return HttpResponse(request)
    values = request.GET.get('email')
    # return HttpResponse(values)
    return render_to_response('anup/selectemail.html', {'user': models.User.objects.all()})


def select(request):
    if request.method == 'POST':
        value = []
        values = (' , '.join(request.POST.getlist('email[]')))
        value.append(values)  # return HttpResponse(values)
        for value in value:
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('anup/roleactivate.html', {
                'user': User,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(User.pk)),
                'token': account_activation_token.make_token(User),
            })

            email1 = EmailMessage(subject, message, to=[value])
            email1.send()
            # return HttpResponse(value)
    return render_to_response('anup/selectemail.html', {'user': models.User.objects.all()})


def activate2(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):

        if account_activation_token.check_token(User, token):
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')


def admininterface(request):

    if request.method == 'POST':
        value = []
        id=request.POST.get('id')
        #member = (','.join(request.POST.get('myCheckboxes')))
        member=request.POST.get('myCheckboxes')
        #value=(''.join(member))

        #return HttpResponse(id,member)
        #return json.dumps(member)
        value.append(member)
        #values=''.join(member)
        #values=map(str,value.split(','))
        #s = value.replace(',', '')
       # s1=len(s)
        #value = ''.join(value)
        #value=value.split()
        #return HttpResponse(value)
        for i in value:
            r1=right(Edit=i[0],Delete=i[2],Display=i[4],Add=i[6])
            r1.save()



    return render_to_response('anup/Dashboard.html', {'role': models.Role.objects.all()})


def profile(request):


    if request.method == 'POST'and request.FILES.get('images'):
            return HttpResponse(request.FILES.get('images'))

            name = request.POST['name']
            # return HttpResponse(name)
            email = request.POST['email']
            # birth_date = request.POST['birth_date']
            address = request.POST['address']
            father_name = request.POST['father_name']
            mother_name = request.POST['mother_name']
            gender = request.POST['gender']
            # path='C:/Users/Dell/Desktop/tecture/anup/static/images/upload/%s'
            image = request.FILES.get('images')
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)

            #path = 'anup.png'
            # initial_path = Profile.image.path.name
            # Profile.image.name = 'C:/static/images/upload/anup.jpg'
            #$new_path = settings.MEDIA_ROOT
            #full_path = os.path.join(new_path, path)
            # Move the file on the filesystem
            # os.rename(new_path)






            Profile.objects.create(
                name=name,
                email=email,
                # birth_date=birth_date,
                address=address,
                father_name=father_name,
                mother_name=mother_name,
                gender=gender,
                image=image,

            )

            return HttpResponse(image)
    #return render(request, 'anup/profile.html')

def adds(request):
 articles = Article.objects.all()
 if request.method == 'POST':
    if request.is_ajax():
        name = request.POST.get('name','')
        description = request.POST.get('description','')
        icon = request.FILES.get('icon','')
        article_new = Article.objects.create(
            name=name,
            description=description,
            icon=icon
        )
        article_new.save()
        return HttpResponse(name)

 return render_to_response('anup/photo.html', {'articles':articles},RequestContext(request))

def permission(request):
    if request.method == 'POST':


        username = request.POST.get('username')

        password = request.POST.get('password')
        role=Role.objects.filter(username=username)
        user=User.objects.filter(password=password)
        right1=right.filter(user__in=user)
        if role.exists():
            if right.objects.all():
                return HttpResponse("Accessbile to your account")

            else:
                return HttpResponse("Not accessible to you")
    return render(request, 'anup/rolelogin.html')

def adminhome(request):
    return render(request,'anup/adminhome.html')

def userright(request):
    return render(request, 'anup/userright.html')

def addrole(request):
    if request.method == 'POST':
        # User.save(commit=False)
        username = request.POST['name']
        email = request.POST['email']
        password=request.POST['password']

        role = request.POST.getlist['role']

        User.objects.create(
            name=username,

            email=email,
            password=password,

            role=role,
        )
    return render(request, 'anup/AddRole.html', {'query_results': models.User.objects.all()})

def active(request,pk):
 t = get_object_or_404(User, pk=pk)
 if t.status==0:
    t.status = 1  # change field
    t.save()

 return render(request, 'anup/AddRole.html', {'query_results': models.User.objects.all()})

def inactive(request,pk):
 t = get_object_or_404(User, pk=pk)
 if t.status==1:
    t.status =0
    t.save()
 return render(request, 'anup/AddRole.html', {'query_results': models.User.objects.all()})

class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'anup/charts.html')

def get_data(request,*args,**kwargs):
    data={
        "sales":10,
        "customer":100,
    }
    return JsonResponse(data)
User = get_user_model()
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 23, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

def work(request):
    if request.method == 'POST':
        Date = request.POST['system']
        froms = request.POST['from']
        to= request.POST['to']
        work.objects.create(
            Date=Date,
            froms=froms,
            to=to,


        )

    return render(request,"anup/work.html",{'role': models.Role.objects.all()})