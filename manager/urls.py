from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    # 책 수요 변화
    path('book/view/', views.book_view, name='book_view'),
    path('book/cover_complete/', views.cover_complete, name='cover_complete'),

    # 도서 신청
    path('book/view/', views.book_view, name='book_view'),
    path('book/view/count', views.book_view_count, name='book_view_count'),
    path('book/request/', views.BookRequestListView.as_view(), name='book_request'),
    path('book/register/<int:book_isbn>/',
         views.BookRegisterView.as_view(), name='book_register'),
    path('book/register/complete/', views.BookRegisterCompleteView.as_view(),
         name='book_register_complete'),

    # 1:1 문의
    path('inquiry/', views.inquiry, name='inquiry'),

    # 수익 현황
    path('subscription/', views.show_subscription, name='subscription'),
    path('api/subscription-count/', views.SubscriptionCountAPIView.as_view(),
         name='api_subscription_count'),  # API 엔드포인트 URL

    # faq
    path('faq/', views.faq, name='faq'),


    # 개인정보처리
    path('privacy_policy/', views.privacy_policy,
         name='privacy_policy'),
]
