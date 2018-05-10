from django.urls import path, re_path

from .views import SettingsGeneralView, SettingsSocialView, FriendsView
from .views import UserBlogView
from .views import UserRegistrationView, UserLoginView, UserInformationView, MainView
from .views import logout_user, search_users, add_post
from .views import test_view, debug_view

urlpatterns = [
    re_path('^$', MainView.as_view(), name='main_view'),
    path('page/<int:page>/', MainView.as_view, name='main_view_with_page'),

    re_path('^signup/$', UserRegistrationView.as_view(), name='signup'),
    re_path('^signin/$', UserLoginView.as_view(), name='signin'),
    re_path('^logout/$', logout_user, name='logout'),

    path('user/<str:username>/', UserInformationView.as_view(), name='user_info'),

    re_path('^settings/general/$', SettingsGeneralView.as_view(), name='settings_general_view'),
    re_path('^settings/social/$', SettingsSocialView.as_view(), name='settings_social_view'),

    re_path('^friends/$', FriendsView.as_view(), name='friends_view'),

    re_path('^search_users/$', search_users, name='user_search'),

    path('user/<str:username>/blog/', UserBlogView.as_view(), name='user_blog_view'),
    path('user/<str:username>/blog/page/<int:page>/', UserBlogView.as_view(), name='user_blog_view_with_page'),

    re_path('^add_post/$', add_post, name='add_post'),

    re_path('^test', test_view, name='test_view'),
    re_path('^debug', debug_view, name='debug_view'),
]
