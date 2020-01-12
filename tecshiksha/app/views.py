from django.shortcuts import render
from .models import Blog,Offer,Workshop
from .forms import ContactForm,InternForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    blogs = Blog.objects.all()

    return render(request, "blog.html", {'blogs': blogs})

def workshops(request):
    workshops = Workshop.objects.all()
    Workshop_Form = ContactForm
    if request.method == 'POST':
        form = Workshop_Form(data=request.POST)

        if form.is_valid():
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            city = request.POST.get('city')
            designation = request.POST.get('designation')
            m_number = request.POST.get('m_number')
            form_content = request.POST.get('form_content')
            template = get_template('contact_template.txt')

            context = {
                'fname' : fname,
                'lname' : lname,
                'email' : email,
                'city' : city,
                'designation':designation,
                'm_number' : m_number,
                'form_content' : form_content
            }
            content = template.render(context)

            email = EmailMessage(
                "New Contact Form Submission for Workshop",
                content,
                "https://www.techshiksha.net" + '',
                ['Info@techshiksha.net'],
                headers = {'Reply-To' : email}
            )
            email.send()
            return render(request,'workshops.html',{'workshops': workshops,})

    return render(request, "workshops.html", {
        'workshops': workshops,
        'form': Workshop_Form,
        })


def courses(request):
    return render(request, "courses.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            city = request.POST.get('city')
            designation = request.POST.get('designation')
            m_number = request.POST.get('m_number')
            form_content = request.POST.get('form_content')
            template = get_template('contact_template.txt')

            context = {
                'fname' : fname,
                'lname' : lname,
                'email' : email,
                'city' : city,
                'designation':designation,
                'm_number' : m_number,
                'form_content' : form_content
            }
            content = template.render(context)

            email = EmailMessage(
                "New Contact Form Submission",
                content,
                "https://www.techshiksha.net" + '',
                ['Info@techshiksha.net'],
                headers = {'Reply-To' : email}
            )
            email.send()
            return render(request,'contact.html')

    return render(request, "contact.html", {
         'form': Contact_Form,
    })

def internship(request):
    Intern_Form = InternForm

    if request.method == 'POST':
        form = Intern_Form(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            m_number = request.POST.get('m_number')
            # cv = request.POST.get('cv')
            city = request.POST.get('city')
            state = request.POST.get('state')
            form_content = request.POST.get('form_content')

            template = get_template('intern_template.txt')
            content = {
                'name': name,
                'email': email,
                'm_number': m_number,
                # 'cv': cv,
                'city': city,
                'state': state,
                'form_content' : form_content,
            }
            content = template.render(content)

            email = EmailMessage(
                "New Form Submission For Internship",
                content,
                "https://www.techshiksha.net" + '',
                ['Info@techshiksha.net'],
                headers = {'Reply-To' : email}
            )
            email.send()
            return render(request,'internship.html')

    return render(request, "internship.html", {
         'form': Intern_Form,
    })

# def contact(request):
#     form_class = ContactForm
#
#     if request.method == 'POST':
#         form = form_class(data=request.POST)
#
#         if form.is_valid():
#             fname = request.POST.get('fname','')
#             lname = request.POST.get('lname','')
#             email = request.POST.get('email','')
#             m_number = request.POST.get('m_number','')
#             form_content = request.POST.get('form_content','')
#
#             template = get_template('contact_template.txt')
#             context = {
#                 'fname': fname,
#                 'lname': lname,
#                 'email': email,
#                 'm_number': m_number,
#                 'form_content' : form_content
#             }
#             content = template.render(context)
#
#             email = EmailMessage(
#                 "New Contact Form Submission",
#                 content,
#                 "https://www.techshiksha.net" + '',
#                 ['Info@techshiksha.net'],
#                 headers = {'Reply-To': email}
#             )
#             email.send()
#             return redirect('contact')
#
#     return render(request, "contact.html", {
#          'form': form_class,
#     })

def ai_page(request):
    AI_Contact_Form = ContactForm
    offers = Offer.objects.all()

    if request.method == 'POST':
        form = AI_Contact_Form(data=request.POST)

        if form.is_valid():
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            city = request.POST.get('city')
            designation = request.POST.get('designation')
            m_number = request.POST.get('m_number')
            form_content = request.POST.get('form_content')
            template = get_template('contact_template.txt')

            context = {
                'fname' : fname,
                'lname' : lname,
                'email' : email,
                'city' : city,
                'designation':designation,
                'm_number' : m_number,
                'form_content' : form_content
            }
            content = template.render(context)

            email = EmailMessage(
                "New Contact Form Submission for AI Course",
                content,
                "https://www.techshiksha.net" + '',
                ['Info@techshiksha.net'],
                headers = {'Reply-To' : email}
            )
            email.send()
            return render(request,'ai_page.html', {'offers': offers},)

    return render(request, "ai_page.html", {
         'form': AI_Contact_Form,
         'offers': offers,
    })

    # return render(request, "ai_page.html", {'offers': offers}, {
    #      'form': AI_Contact_Form,
    # })

def iot_page(request):
    IoT_Contact_Form = ContactForm
    offers = Offer.objects.all()

    if request.method == 'POST':
        form = IoT_Contact_Form(data=request.POST)

        if form.is_valid():
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            city = request.POST.get('city')
            designation = request.POST.get('designation')
            m_number = request.POST.get('m_number')
            form_content = request.POST.get('form_content')
            template = get_template('contact_template.txt')

            context = {
                'fname' : fname,
                'lname' : lname,
                'email' : email,
                'city' : city,
                'designation':designation,
                'm_number' : m_number,
                'form_content' : form_content
            }
            content = template.render(context)

            email = EmailMessage(
                "New Contact Form Submission for IOT Course",
                content,
                "https://www.techshiksha.net" + '',
                ['Info@techshiksha.net'],
                headers = {'Reply-To' : email}
            )
            email.send()
            return render(request,'IoT_page.html',{'offers': offers})

    return render(request, "IoT_page.html", {
        'offers': offers,
        'form': IoT_Contact_Form,
    })

    # return render(request, "ai_page.html", {'offers': offers}, {
    #      'form': AI_Contact_Form,
    # })


def web_designing_page(request):
    WD_Contact_Form = ContactForm
    offers = Offer.objects.all()

    if request.method == 'POST':
        form = WD_Contact_Form(data=request.POST)

        if form.is_valid():
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            city = request.POST.get('city')
            designation = request.POST.get('designation')
            m_number = request.POST.get('m_number')
            form_content = request.POST.get('form_content')
            template = get_template('contact_template.txt')

            context = {
                'fname' : fname,
                'lname' : lname,
                'email' : email,
                'city' : city,
                'designation':designation,
                'm_number' : m_number,
                'form_content' : form_content
            }
            content = template.render(context)

            email = EmailMessage(
                "New Contact Form Submission for Web Designing Course",
                content,
                "https://www.techshiksha.net" + '',
                ['Info@techshiksha.net'],
                headers = {'Reply-To' : email}
            )
            email.send()
            return render(request,'web_designing_page.html',{'offers': offers})

    return render(request, "web_designing_page.html", {
        'offers': offers,
        'form': WD_Contact_Form,
    })

    # return render(request, "ai_page.html", {'offers': offers}, {
    #      'form': AI_Contact_Form,
    # })

def python_page(request):
    PY_Contact_Form = ContactForm
    offers = Offer.objects.all()

    if request.method == 'POST':
        form = PY_Contact_Form(data=request.POST)

        if form.is_valid():
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            city = request.POST.get('city')
            designation = request.POST.get('designation')
            m_number = request.POST.get('m_number')
            form_content = request.POST.get('form_content')
            template = get_template('contact_template.txt')

            context = {
                'fname' : fname,
                'lname' : lname,
                'email' : email,
                'city' : city,
                'designation':designation,
                'm_number' : m_number,
                'form_content' : form_content
            }
            content = template.render(context)

            email = EmailMessage(
                "New Contact Form Submission for Python Course",
                content,
                "https://www.techshiksha.net" + '',
                ['Info@techshiksha.net'],
                headers = {'Reply-To' : email}
            )
            email.send()
            return render(request,'python_page.html',{'offers': offers})

    return render(request, "python_page.html", {
        'offers': offers,
        'form': PY_Contact_Form,
    })

    # return render(request, "ai_page.html", {'offers': offers}, {
    #      'form': AI_Contact_Form,
    # })

def android_app_page(request):
    AND_Contact_Form = ContactForm
    offers = Offer.objects.all()

    if request.method == 'POST':
        form = AND_Contact_Form(data=request.POST)

        if form.is_valid():
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            city = request.POST.get('city')
            designation = request.POST.get('designation')
            m_number = request.POST.get('m_number')
            form_content = request.POST.get('form_content')
            template = get_template('contact_template.txt')

            context = {
                'fname' : fname,
                'lname' : lname,
                'email' : email,
                'city' : city,
                'designation':designation,
                'm_number' : m_number,
                'form_content' : form_content
            }
            content = template.render(context)

            email = EmailMessage(
                "New Contact Form Submission for Android App Development Course",
                content,
                "https://www.techshiksha.net" + '',
                ['Info@techshiksha.net'],
                headers = {'Reply-To' : email}
            )
            email.send()
            return render(request,'android_app_page.html', {'offers': offers})

    return render(request, "android_app_page.html", {
        'offers': offers,
        'form': AND_Contact_Form,
    })

    # return render(request, "ai_page.html", {'offers': offers}, {
    #      'form': AI_Contact_Form,
    # })

def ios_app_page(request):
    IoS_Contact_Form = ContactForm
    offers = Offer.objects.all()

    if request.method == 'POST':
        form = IoS_Contact_Form(data=request.POST)

        if form.is_valid():
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            city = request.POST.get('city')
            designation = request.POST.get('designation')
            m_number = request.POST.get('m_number')
            form_content = request.POST.get('form_content')
            template = get_template('contact_template.txt')

            context = {
                'fname' : fname,
                'lname' : lname,
                'email' : email,
                'city' : city,
                'designation':designation,
                'm_number' : m_number,
                'form_content' : form_content
            }
            content = template.render(context)

            email = EmailMessage(
                "New Contact Form Submission for IOS App Development Course",
                content,
                "https://www.techshiksha.net" + '',
                ['Info@techshiksha.net'],
                headers = {'Reply-To' : email}
            )
            email.send()
            return render(request,'ios_app_page.html', {'offers': offers})

    return render(request, "ios_app_page.html", {
        'offers': offers,
        'form': IoS_Contact_Form,
    })

    # return render(request, "ai_page.html", {'offers': offers}, {
    #      'form': AI_Contact_Form,
    # })

# def error_404(request):
#         data = {}
#         return render(request,'error_404.html', data)
#
# def error_500(request):
#         data = {}
#         return render(request,'error_500.html', data)
