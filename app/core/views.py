from django.views.generic import TemplateView, DetailView, ListView, FormView
from .models import Service, Project, About, WhyChooseUs, Process, Gallery, News, Team, Hero
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render, redirect

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["hero"] = Hero.objects.first()
        context["services"] = Service.objects.all()[:6]
        context["projects"] = Project.objects.all()[:4]
        context["about"] = About.objects.first()
        context["why_choose_us"] = WhyChooseUs.objects.first()
        context["process"] = Process.objects.first()
        context["gallery"] = Gallery.objects.all()[:3]
        context["news"] = News.objects.filter(is_main_page = True)[:3]
        context["team"] = Team.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Mesajınız göndərildi!')
            return redirect(request.path + '#contact-form')

    
class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context["about"] = About.objects.first()
        return context
    
class ServicePageView(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super(ServicePageView, self).get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        return context
    
class ServiceDetailPageView(DetailView):
    template_name = 'service-detail.html'
    model = Service
    context_object_name = "service"
    
    def get_context_data(self, **kwargs):
        context = super(ServiceDetailPageView, self).get_context_data(**kwargs)
        context["other_services"] = Service.objects.exclude(pk = self.get_object().pk).order_by("-pk")[:5]
        return context
    
class ProjectPageView(TemplateView):
    template_name = 'projects.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectPageView, self).get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context
    
class ProjectDetailPageView(DetailView):
    template_name = 'project-detail.html'
    model = Project
    context_object_name = "project"
    
class NewsPageView(ListView):
    template_name = 'news.html'
    paginate_by = 8
    model = News
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super(NewsPageView, self).get_context_data(**kwargs)
        context["last_news"] = News.objects.all()[:3]
        return context

class NewsDetailPageView(DetailView):
    template_name = 'news-detail.html'
    model = News
    context_object_name = "news"
    
    def get_context_data(self, **kwargs):
        context = super(NewsDetailPageView, self).get_context_data(**kwargs)
        context["last_news"] = News.objects.exclude(pk = self.get_object().pk)[:3]
        return context
    
class GalleryPageView(ListView):
    template_name = 'gallery.html'
    # paginate_by = 8
    model = Gallery
    context_object_name = 'gallery'

class ContactPageView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    # success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Mesajınız göndərildi!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return self.request.path