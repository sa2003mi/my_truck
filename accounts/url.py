from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from django.urls import reverse_lazy

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/' , auth_views.LogoutView.as_view() , name = 'logout'),
    path('login/' , auth_views.LoginView.as_view(template_name='login.html') , name = 'login'),
    path('reset/',
                    auth_views.PasswordResetView.as_view(
                        template_name='password_reset.html',
                        email_template_name='password_reset_email.html',
                        subject_template_name='password_reset_subject.txt', 
                        success_url=reverse_lazy('accounts:password_reset_done')), name = 'password_reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html', success_url=reverse_lazy('accounts:password_reset_complete')),
         name='password_reset_confirm'),

    path('reset/complete/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html',success_url=reverse_lazy('accounts:password_change_done')),
         name='password_change'),

    path('settings/password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),

    
    path('settings/account/done/', auth_views.PasswordChangeDoneView.as_view(template_name='my_account_change_done.html'), name='my_account_change_done'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/change_password', views.change_password, name='change_password'),
]
