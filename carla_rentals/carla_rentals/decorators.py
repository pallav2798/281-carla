

import traceback
from django.shortcuts import redirect, render


def check_session(func):
    def wrap(request, *args, **kwargs):
        try:
            if request.request.user.is_authenticated:
                return func(request, *args, **kwargs)
            else:
                return redirect('login-page')

            
        except Exception as e:
            print(traceback.print_exc())
            return render(request.request, 'webapp/404-page.html')

    
    wrap.__doc__ = func.__doc__
    wrap.__name__ = func.__name__
    return wrap
