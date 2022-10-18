from .models import UserProflie


def get_proflie(request):
    if request.user.is_authenticated:
        proflie = UserProflie.objects.get(user=request.user)
        return {"proflie": proflie}
    else:
        return {}
