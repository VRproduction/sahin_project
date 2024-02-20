from django.views.generic import TemplateView, DetailView
from .models import Service, Project, About, WhyChooseUs, Process, Gallery, News, Team

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["services"] = Service.objects.all()[:6]
        context["projects"] = Project.objects.all()[:4]
        context["about"] = About.objects.first()
        context["why_choose_us"] = WhyChooseUs.objects.first()
        context["process"] = Process.objects.first()
        context["gallery"] = Gallery.objects.all()[:3]
        context["news"] = News.objects.filter(is_main_page = True)[:3]
        context["team"] = Team.objects.all()[:2]
        return context
    
class ServiceDetailPageView(DetailView):
    template_name = 'service-detail.html'
    model = Service
    context_object_name = "service"
    
    def get_context_data(self, **kwargs):
        context = super(ServiceDetailPageView, self).get_context_data(**kwargs)
        context["other_services"] = Service.objects.exclude(pk = self.get_object().pk).order_by("-pk")[:5]
        return context
    
class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context["about"] = About.objects.first()
        return context