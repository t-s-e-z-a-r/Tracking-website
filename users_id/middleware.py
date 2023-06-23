from django.http import HttpResponseForbidden

class RestrictPortAndPathMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.restricted_port = 8080
        self.restricted_paths = ['/page1/', '/page2/']

    def __call__(self, request):
        if request.META['SERVER_PORT'] == str(self.restricted_port) and request.path_info in self.restricted_paths:
            return HttpResponseForbidden('Access Denied')

        return self.get_response(request)
