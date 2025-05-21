from allauth.socialaccount.models import SocialAccount

def social_data(request):
    data = None
    if request.user.is_authenticated:
        try:
            social_account = SocialAccount.objects.get(user=request.user)
            data = social_account.extra_data
        except SocialAccount.DoesNotExist:
            data = None
    return {'social_data': data}