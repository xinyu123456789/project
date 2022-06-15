from django.views.generic import *
from django.urls import reverse
from .models import *
from django.contrib.auth.mixins import PermissionRequiredMixin

# 教學計劃列表
class TopicList(ListView):
    model = Topic
    ordering = ['-created']
    paginate_by = 20        #每頁教學計劃數量

# 新增教學計劃
class TopicNew(CreateView):
    model = Topic
    fields = ['subject', 'classes', 'content']

    def get_success_url(self):
        return reverse('topic_list')

    def form_valid(self, form):
        # 自動將目前使用者填入討論主題的作者欄
        form.instance.author = self.request.user
        return super().form_valid(form)

# 檢視教學計畫
class TopicView(DetailView):
    model = Topic

# 刪除教學計畫
class TopicDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'topic.delete_topic'
    model = Topic
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('topic_list')

# 123