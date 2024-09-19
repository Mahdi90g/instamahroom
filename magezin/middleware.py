from .models import ipadd

class savemid:
    def __init__(self, get_response):
        self.get_response = get_response



    def __call__(self, request):

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if  x_forwarded_for:
            ip =  x_forwarded_for.split(',')[0]
        else:
            ip =  request.META.get('REMOTE_ADDR')
        try:
            ip_add = ipadd.objects.get(ip_add=ip)  
        except ipadd.DoesNotExist :
            ip_add = ipadd(ip_add=ip)
            ip_add.save()
        request.user.ip_address = ip_add             



        response = self.get_response(request)



        return response    