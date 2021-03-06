from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView, RedirectView
from django.views.generic.base import View
from .forms import ProjectForm, QueryProjectForm, UserForm, USRegister, US
from .models import Project, Usuario, ProjectUser
from itertools import chain
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.functional import cached_property

# Create your views here.

'''
Generic class views are a form of making the application development easier and faster by using pre-made views.
Those views have methods and variables ready for it's cenario.
To learn more about class based views refer to: https://docs.djangoproject.com/en/2.0/ref/class-based-views/
'''


class IndexView(View):
    template_name = 'ctsp/index.html'

    def post(self, request, *args, **kwargs):
        """
        This function receives the post method comming from the IndexView.
        The return is a JSON file returning all the elements of the searched Project.
        To learn about "Q classes" refer to: https://docs.djangoproject.com/en/2.0/topics/db/queries/
        To learn about JSON file structure refer to: https://www.json.org/ and http://json.org/example.html
        """

        if self.request.is_ajax():
            search_text = request.POST.get('search_text')

            try:
                project = Project.objects.filter(
                    Q(project_name__icontains=search_text) | Q(id__icontains=search_text))
            except ValueError:
                project = Project.objects.filter(
                    project_name__icontains=search_text)

            context = []
            for i in range(0, len(project)):
                context.append({
                    'project_pk': project[i].id,
                    'project_name': project[i].project_name,
                    'project_start': project[i].project_start_date,
                    'project_end': project[i].project_final_date,
                })
            return JsonResponse(context, safe=False)

        return render(request, self.template_name)

    def get(self, request):
        form = ProjectForm()
        query = QueryProjectForm()
        context = {'query': query, 'form': form}
        return render(request, self.template_name, context)


class CreatePbacklogView(TemplateView):
    template_name = "ctsp/create_pbacklog.html"


class CreateSprintView(TemplateView):
    template_name = "ctsp/create_sprint.html"


class AssignMembersView(TemplateView):
    template_name = "ctsp/assign_members.html"


class CreateProjectView(View):
    """
    This redirect view is used as a middleware view to creating a unique URL for the project.
    The URL contains the actual database PK for the project which is generated at the momment it is saved.
    This primary key can be encrypted in the future.
    """

    pattern_name = 'project_welcome'

    def get(self, request):
        return render(request, 'ctsp:project_welcome')

    def post(self, request, *args, **kwargs):
        form = ProjectForm(request.POST)
        if form.is_valid():
            print("form valid")
            project = form.save(commit=True)
            return redirect('ctsp:project_welcome', pk=project.pk, permanent=False)

        # return redirect('ctsp:index')


class WelcomeProjectView(TemplateView):
    template_name = 'ctsp/welcome_created.html'

    def get_context_data(self, **kwargs):
        context = super(WelcomeProjectView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.filter(pk=context['pk'])
        return context


class AboutView(TemplateView):
    template_name = 'ctsp/about.html'


class CreateMembers(TemplateView):
    template_name = 'ctsp/create_members.html'


class RegisterUser(View):
    template_name = 'ctsp/register_user.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = UserForm(request.POST)

        dados_form = form.data

        if form.is_valid():
            novo_usuario = User.objects.create_user(
                dados_form['nome'], dados_form['email'], dados_form['senha'])
            usuario = Usuario(user_name=dados_form['nome'],
                              user_last_name=dados_form['sobrenome'],
                              user_birthday=dados_form['data'],
                              user_cellphone_number=dados_form['telefone'],
                              user_habilities=dados_form['habilidades'],
                              user_usuario=novo_usuario)

            usuario.save()
            return redirect('ctsp:index')

        return render(request, self.template_name, {"form": form})


class LogInMember(View):
    template_name = 'ctsp/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return redirect("ctsp:welcome_login")


class ProjectRedirect(View):
    template_name = 'ctsp/welcome_login.html'

    def post(self, request):
        pk = request.POST.get("select_project_pk")
        if request.POST.get('_product'):
            return redirect('ctsp:product_backlog', pk=pk)
        if request.POST.get('_team'):
            return redirect('ctsp:assign_members', pk=pk)
        else:
            return render(request, self.template_name)


class AssignMembers(TemplateView):
    template_name = 'ctsp/assign_members.html'

    def get_context_data(self, **kwargs):
        context = super(AssignMembers, self).get_context_data(**kwargs)
        context['users'] = Usuario.objects.all()
        return context

    def post(self, request, **kwargs):
        if self.request.is_ajax():
            proj_pk = super(AssignMembers, self).get_context_data(**kwargs)['pk'];
            user_pk = request.POST['member']

            # just in case...
            user = Usuario.objects.get(id=user_pk)
            print(user.user_name)
            project = Project.objects.get(id=proj_pk)

            instance = ProjectUser(member_id=user_pk, project_id=proj_pk)
            instance.save()
            return JsonResponse({'user': user.user_name, 'project': project.project_name}, safe=False)


class ProductBacklog(TemplateView):
    template_name = 'ctsp/product_backlog.html'

    def get_context_data(self, **kwargs):
        context = super(ProductBacklog, self).get_context_data(**kwargs)
        context['form'] = USRegister()
        return context

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            form = USRegister(request.POST)
            if form.is_valid():
                # create instance to save and check
                instance = form.save(commit=False)
                pk = super(ProductBacklog, self).get_context_data(**kwargs)['pk']
                instance.us_project = Project.objects.get(id=pk)
                form.save()

                # creating feedback dict
                feedback = dict()
                for key in form.cleaned_data:
                    feedback[key] = form.cleaned_data[key]

                return JsonResponse({'feedback': feedback, 'message': 'your US was registered.'}, safe=False)
            else:
                return JsonResponse({'message': 'Check your form inputs'}, safe=False)


class WelcomeLogin(TemplateView):
    template_name = 'ctsp/welcome_login.html'

    # "get_context_data" not needed anymore, substituted by the "projects" function above

    # def get_context_data(self, **kwargs):
    #     context = super(WelcomeLogin, self).get_context_data(**kwargs)
    #     context['projects'] = Project.objects.all()
    #     return context

    @cached_property
    def projects(self):
        return Project.objects.only('project_name', 'pk')

    def post(self, request):
        return render(request, self.template_name)
