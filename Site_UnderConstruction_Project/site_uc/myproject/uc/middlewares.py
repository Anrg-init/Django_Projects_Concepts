# from django.shortcuts import render
# from . import models

# class UnderContructionMiddleware:

#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("middleware is initializing")

#     def __call__(self, request):

#         if request.user.is_staff:
#             print("test admin")
#             return self.get_response(request)
        
#         try:
#             uc = models.UnderContstruction.objects.first()
#             if uc and uc.is_uc:
#                 context = {
#                     'ucnote': uc.uc_note
#                 }
#                 print("nice")
#                 return render(request, 'uc/uc.html', context)
#         except:
#             pass

#         print("html page test")
#         return self.get_response(request)


# # method2
# from django.shortcuts import render
# from . import models


# class UnderContructionMiddleware:

#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("middleware is initializing")

#     def __call__(self, request):

#         # allow admin panel always
#         if request.path.startswith('/admin'):
#             return self.get_response(request)

#         # allow staff users
#         if request.user.is_authenticated and request.user.is_staff:
#             return self.get_response(request)

#         uc = models.UnderContstruction.objects.first()

#         if uc and uc.is_uc:
#             return render(request, 'uc/uc.html', {'ucnote': uc.uc_note})

#         return self.get_response(request)



# method3

from django.shortcuts import render
from decouple import config
from .models import UnderContstruction


class UnderContructionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print("UnderConstructionMiddleware loaded")

    def __call__(self, request):


        if request.path.startswith('/admin'):
            return self.get_response(request)


        bypass_key = config('MAINTENANCE_BYPASS_KEY')


        key_from_url = request.GET.get('u')

        if key_from_url and key_from_url == bypass_key:
            request.session['bypass_maintenance'] = True
            request.session.set_expiry(0)  


        if request.session.get('bypass_maintenance', False):
            return self.get_response(request)

        uc = UnderContstruction.objects.first()

        if uc and uc.is_uc:
            return render(request, 'uc/uc.html', {
                'ucnote': uc.uc_note
            })

        return self.get_response(request)
