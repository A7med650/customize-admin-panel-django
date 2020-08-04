# customize-admin-panel-django

1. pip install https://github.com/Barukimang/django-jet/archive/dev.zip
2. pip install --upgrade google-api-python-client
3. pip install oauth2client

insert the code in settings.py:

```
INSTALLED_APPS = (
    ...
    'jet',
    'django.contrib.admin',
)
```

insert the code in urls.py:
```
urlpatterns [
    '',
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', include(admin.site.urls)),
    ...
]
```

4. python manage.py migrate jet
5. python manage.py collectstatic

## Dashboard installation

insert the code in settings.py:
```
INSTALLED_APPS = (
    ...
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    ...
)
```

insert the code in urls.py:
```
urlpatterns [
    '',
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', include(admin.site.urls)),
    ...
]
```

insert the code in settings.py:
```
X_FRAME_OPTIONS = 'SAMEORIGIN'
```

6. python manage.py migrate dashboard
7. python manage.py collectstatic

## Documentation
https://jet.readthedocs.io/en/latest/
