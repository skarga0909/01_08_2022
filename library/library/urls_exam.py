from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
# from library.view_exam import BookQuerysetFilterViewSet
# from library.view_exam import BookListAPIView

# from library.view_exam import BookCustomViewSet
# from authors.views import AuthorViewSet,BookViewSet,BiographyViewSet

# from library.view_exam import BookListAPIView, BookCreateAPIView, BookUpdateAPIView, BookDestroyAPIView, \
#     BookRetrieveAPIView
# from library.view_exam import get
# from library.view_exam import BookViewSet
# BookLimitOffsetPaginatonViewSet
# from library.view_exam import get
# from library.view_exam import BookCustomViewSet
# from library.view_exam import BookListAPIView
# from library.view_exam import BookLimitOffsetPaginatonViewSet
# from library.view_exam import BookModelViewSet
# from library.view_exam import BookDjangoFilterViewSet
# from library.view_exam import BookAPIView
# from library.view_exam import get


router = DefaultRouter()
# from library.view_example import BookModelViewSet
# from library.view_example import BookModelViewSet
# router.register('book_f', BookModelViewSet, basename='book_f')
# router.register('book_f', BookModelViewSet)

# router = SimpleRouter()
# router.register('book_f', BookDjangoFilterViewSet)
# router.register('book_p', BookLimitOffsetPaginatonViewSet)
# router.register('biography', BiographyViewSet)


# from library.view_exam import BookCreateAPIView,BookListAPIView,BookRetrieveAPIView,BookDestroyAPIView,BookListAPIView,BookUpdateAPIView


# level 3
# router.register('book', BookViewSet, basename='book')

# level 4
# router.register('book', BookViewSet)

# level 5
# router.register('book', BookCustomViewSet)

#Filter
# router.register('book_filter', BookQuerysetFilterViewSet, basename='book_filter')


#
# router.register('book', BookViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/', include(router.urls)),

    # level 1
    # path('api/book', BookAPIView.as_view()),
    # path('api/book', get),

    # level 2
    # path('api/list/', BookListAPIView.as_view()),
    # path('api/create/', BookCreateAPIView.as_view()),
    # path('api/update/<int:pk>/', BookUpdateAPIView.as_view()),
    # path('api/delete/<int:pk>/', BookDestroyAPIView.as_view()),
    # path('api/detail/<int:pk>/', BookRetrieveAPIView.as_view()),


    # # level 3 - 5
    path('api/', include(router.urls)),

    # filter part_2
    # path('api/<str:name>/', BookListAPIView.as_view()),
    #
    # path('api/', include(router.urls)),


]
# Footer
