class editmixin():
    def dispatch(self , request , *args , **kwargs):
        if request.user.is_superuser:
            self.fields=['title','body','status','conformation']
        else:
             self.fields=['title','body','status']
        return super().dispatch(request , *args , *kwargs)        
