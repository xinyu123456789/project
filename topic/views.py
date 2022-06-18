from django.views.generic import *
from django.urls import reverse
from .models import *
from django.contrib.auth.mixins import PermissionRequiredMixin


# 學校列表
class TopicList(ListView):
    model = Topic
    ordering = ['-created']
    paginate_by = 20        #每頁學校數量

    def get_queryset(self):
        query = self.request.GET.get('query')
        query1 = self.request.GET.get('query1')
        query2 = self.request.GET.get('query2')
        if query:
            item = Topic.objects.filter(content__icontains=query)
        if query1:
            if query1 != "none" and query2 != "none":
                item = Topic.objects.filter(subject=int(query1),classes=int(query2))
            elif query1 != "none":
                item = Topic.objects.filter(subject=int(query1))
            elif query2 != "none":
                item = Topic.objects.filter(classes=int(query2))
            else:
                item = Topic.objects
        if (not query) and (not query1) and (not query2):
            item = Topic.objects

        return item.order_by('content')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('query') or ""
        return ctx


# 新增學校
class TopicNew(CreateView):
    model = Topic
    fields = ['content', 'subject', 'classes',  'road', 'picture', 'slink1', 'slink2']

    def get_success_url(self):
        return reverse('topic_list')

    

# 檢視
class TopicView(DetailView):
    model = Topic

# 刪除學校
class TopicDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'topic.delete_topic'
    model = Topic
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('topic_list')

class TopicLocation(ListView):
    model = Location
    template_name = 'topic_location.html'

# 查詢學校

# 123