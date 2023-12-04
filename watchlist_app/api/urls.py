from django.urls import path
from watchlist_app.api.views import MovieListAV, MovieDetailAV, StreamPlatformListAV,StreamPlatformDetailAV, ReviewList, ReviewDetails,ReviewCreate
urlpatterns = [

    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie-detail'),

    path('stream/', StreamPlatformListAV.as_view(), name="stream"),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),

    path('stream/review/<int:pk>/',ReviewDetails.as_view(), name="reivew-detail" ),
    # path('reivews/<int:pk>/',ReviewDetails.as_view(), name="reivew-details" ),
    path('stream/<int:pk>/review',ReviewList.as_view(), name="reivew-lists" ),
    path('stream/<int:pk>/review-create',ReviewCreate.as_view(), name="reivew-create" ),
]

