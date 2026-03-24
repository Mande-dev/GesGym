from django.http import HttpResponseForbidden


def role_required(allowed_roles):
    def decorator(view_func):

        def wrapper(request, *args, **kwargs):

            if request.role not in allowed_roles:
                return HttpResponseForbidden()
            
            if not request.role or request.role not in allowed_roles:
                return HttpResponseForbidden()

            return view_func(request, *args, **kwargs)

        return wrapper
    return decorator