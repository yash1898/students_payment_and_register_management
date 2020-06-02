from . import views
from django.urls import path,include

app_name = 'register'

urlpatterns = [
    path('register/',views.Register_View,name='register'),
    path('view_students/',views.view_students,name='view_students'),
    path('view_detail(?P<int:pid>)/',views.view_detail,name='view_detail'),
    path('view_first_students/',views.view_first_students,name='view_first_students'),
    path('view_second_students/',views.view_second_students,name='view_second_students'),
    path('view_third_students/',views.view_third_students,name='view_third_students'),
    path('view_forth_students/',views.view_forth_students,name='view_forth_students'),
    path('view_page/',views.view_page,name='view_page'),
    path('edit_students(?P<int:pid>)/',views.edit_students,name='edit_students'),
    path('delete_students(?P<int:pid>)/',views.delete_students,name='delete_students'),
    path('payment/',views.payment,name='payment'),
    path('payment/paid_fees/',views.paid_fees,name='paid_fees'),
    path('payment/paid_fees_zero/',views.paid_fees_zero,name='paid_fees_zero'),
    path('payment/paid_fees_partial/',views.paid_fees_partial,name='paid_fees_partial'),
    path('payment/paid_fees_first/',views.paid_fees_first,name='paid_fees_first'),
    path('payment/paid_fees_first_partial/',views.paid_fees_first_partial,name='paid_fees_first_partial'),
    path('payment/paid_fees_firstz/',views.paid_fees_firstz,name='paid_fees_firstz'),
    path('payment/paid_fees_second/',views.paid_fees_second,name='paid_fees_second'),
    path('payment/paid_fees_second_partial/',views.paid_fees_second_partial,name='paid_fees_second_partial'),
    path('payment/paid_fees_secondz/',views.paid_fees_secondz,name='paid_fees_secondz'),
    path('payment/paid_fees_third/',views.paid_fees_third,name='paid_fees_third'),
    path('payment/paid_fees_third_partial/',views.paid_fees_third_partial,name='paid_fees_third_partial'),
    path('payment/paid_fees_thirdz/',views.paid_fees_thirdz,name='paid_fees_thirdz'),
    path('payment/paid_fees_forth/',views.paid_fees_forth,name='paid_fees_forth'),
    path('payment/paid_fees_forth_partial/',views.paid_fees_forth_partial,name='paid_fees_forth_partial'),
    path('payment/paid_fees_forthz/',views.paid_fees_forthz,name='paid_fees_forthz'),
]