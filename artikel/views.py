from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from artikel.models import Kategori, ArtikelBlog
from artikel.forms import KategoriForms, ArtikelForms

# Create your views here.

def artikel_list(request):
    template_name="artikel_list.html"
    kategori = Kategori.objects.all()
    artikel = ArtikelBlog.objects.all()
    context = {
        "kategori":kategori,
        "artikel":artikel,
    }

    return render(request, template_name, context)

# admin #

@login_required(login_url='/auth-login')
def admin_kategori_list(request):
    template_name = "dashboard/admin/kategori_list.html"
    kategori = Kategori.objects.all()
    context = {
        'kategori':kategori,
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_kategori_tambah(request):
    template_name = "dashboard/admin/kategori_forms.html"

    if request.method == "POST":
        forms = KategoriForms(request.POST)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            return redirect(admin_kategori_list)
        
    forms = KategoriForms()
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_kategori_update(request, id_kategori):
    template_name = "dashboard/admin/kategori_forms.html"
    kategori = Kategori.objects.get(id=id_kategori)

    if request.method == "POST":
        forms = KategoriForms(request.POST, instance=kategori)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            return redirect(admin_kategori_list)
        
    forms = KategoriForms(instance=kategori)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_kategori_delete(request, id_kategori):
    try:
        Kategori.objects.get(id=id_kategori).delete()
    except:
        pass

    return redirect(admin_kategori_list)


# Artikel Blog #

@login_required(login_url='/auth-login')
def admin_artikel_list(request):
    template_name = "dashboard/admin/artikel_list.html"
    artikel = ArtikelBlog.objects.all()
    context = {
        'artikel':artikel,
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"
    
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            return redirect(admin_artikel_list)
        
    forms = ArtikelForms()
    context = {
        "forms":forms
    }
    return render(request, template_name, context)


@login_required(login_url='/auth-login')
def admin_artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_forms.html"
    artikel = ArtikelBlog.objects.get(id=id_artikel)

    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            return redirect(admin_artikel_list)
        
    forms = ArtikelForms(instance=artikel)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_artikel_delete(request, id_artikel):
    try:
        ArtikelBlog.objects.get(id=id_artikel).delete()
    except:
        pass

    return redirect(admin_artikel_list)