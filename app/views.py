# main settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.db.models import Count

# messages
from django.contrib import messages

# email
from django.core.mail import send_mail

# pagination
from django.core.paginator import Paginator

# twilio:
from twilio.rest import Client

# models:
from . models import Schedule, Faq, Coach, History, Post

# forms:
from . forms import FeedbackForm, PostForm



def main(request):
    """ главная страница """
    posts = Post.objects.filter(active=True)[:3]
    return render(request, 'index.html', {'posts': posts,})

def news(request):
    """ страница новостей """
    posts = Post.objects.filter(active=True)
    posts_new = Post.objects.filter(active=True)[:3]
    paginator = Paginator(posts, 7)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'news.html', {'posts': posts,
                                         'posts_new': posts_new,
                                         })  


def post_detail(request, slug):
    """ страница новости блога """
    post = get_object_or_404(Post, slug=slug)
    # count_comments = Comment.objects.filter(post=post).count()
    user = request.user

    # comments
    # comments = post.comments.filter(parent__isnull=True).select_related('user')
    # comments = Comment.objects.select_related('user').filter(post=post, parent__isnull=True)

    #Comments Form
    # if request.method == 'POST':
    #     form_comment = CommentForm(request.POST)
    #     if form_comment.is_valid():
    #         parent_obj = None
    #         try:
    #             parent_id = int(request.POST.get('parent_id'))
    #         except:
    #             parent_id = None
    #         if parent_id:
    #             parent_obj = Comment.objects.get(id=parent_id)

    #         comment = form_comment.cleaned_data['body']    
    #         if parent_obj:
    #            Comment(user=user, body=comment, parent=parent_obj, post=post).save()
    #         else:
    #            Comment(user=user, body=comment, post=post).save()
            
    #         # pip install twilio 
    #         # account_sid = settings.TWILIO_ACCOUNT_SID
    #         # auth_token = settings.TWILIO_AUTH_TOKEN
    #         # client = Client(account_sid, auth_token)

    #         # message = client.messages \
    #         #                 .create(
    #         #                      body=f"Здарова {request.user.first_name}, вы оставили комментарий на сайте Дельта. - {comment}",
    #         #                      from_='+13865304445',
    #         #                      to='+79244396120'
    #         #                  )

    #         # print(message.sid)    
    #         # print(message.status)
    #         # print(message.to)
    #         return HttpResponseRedirect(reverse('app:detail', args=[slug]))
    # else:
    #     form_comment = CommentForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.image = post.image
            post.save()
            return redirect(reverse('app:detail', kwargs = {
                'slug': post.slug
            }))
    else:
        form = PostForm(instance=post)
        posts = Post.objects.filter(active=True)[:3]
    return render(request, 'post-detail.html', {'form': form, 
                                                "post":post, 
                                                'posts': posts, 
                                                })           
                        
# class CommentsDeleteView(DeleteView):
#     """ удалить комментарий """
#     model = Comment
#     # success_url = reverse_lazy('app:main')

#     def delete(self, request, *args, **kwargs):
#         # пользователь не может удалять чужой контент
#         self.object = self.get_object()
#         if self.request.user != self.object.user:
#             return self.handle_no_permission()
#         success_url = self.get_success_url()
#         self.object.delete()
#         return HttpResponseRedirect(success_url)

#     def get_success_url(self):
#         return reverse('app:main')         

def contact(request):
    """ страница контакты """
    schedules = Schedule.objects.filter(active=True)
    if request.method == 'GET':
        form = FeedbackForm()
    else:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            try:
                form.save()

                title = "%s. %s -  %s" % ('Получено сообщение с контактной формы', name, phone)
                contact_message = "%s \nКонтакты: %s, %s \nТекст сообщения: %s" % (name, phone, email, text)
                send_mail(title, contact_message, 'dfcdelta@gmail.com', ['dfcdelta@gmail.com'])

                form = FeedbackForm()
                # messages.add_message(request, messages.INFO, f'Форма успешно отправлена, скоро с вами свяжемся по телефону {phone}')
            except BadHeaderError:
                return HttpResponse('Найден недопустимый заголовок')
            return HttpResponseRedirect('/thanks/')
    return render(request, "contact.html", {'form': form, 'schedules':schedules})
 

def thanks(request):
    """ успешная отправка формы """
    return render(request, 'email/thanks.html')  


def about(request):
    """ страница о клубе """
    coachs = Coach.objects.filter(active=True)
    historys = History.objects.filter(active=True)
    return render(request, 'about.html', {'coachs': coachs, 'historys': historys})     

def shop(request):
    return render(request, 'shop.html')

def team(request):
    return render(request, 'team.html')

def gallery(request):
    """ страница галерея """
    return render(request, 'gallery.html')    

def faq(request):
    """ страница faq """
    onefaq = Faq.objects.filter(active=True).values("title", "ordernumber", 'text')[:1]
    faqs = Faq.objects.filter(active=True).values("title", "ordernumber", 'text')[1:]
    return render(request, 'faq.html', {'faqs': faqs, 'onefaq': onefaq,})  

def support(request):
    return render(request, 'support.html')      

def privacy(request):
    return render(request, 'privacy.html')     

def pageNotFound(request, exception):
    """ 404 ошибка """
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')    