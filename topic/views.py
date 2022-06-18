from django.views.generic import *
from django.urls import reverse
from .models import *
from django.contrib.auth.mixins import PermissionRequiredMixin


# 學校列表
class TopicList(ListView):
    model = Topic
    ordering = ['-created']
    paginate_by = 20        #每頁學校數量

# 新增學校
class TopicNew(CreateView):
    model = Topic
    fields = ['subject', 'classes', 'content']

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

class TopicLocation(DetailView):
    model = Topic
    template_name = 'topic_location.html'

# 查詢學校
class TopicSearch(DetailView):
    model = Topic

# 123