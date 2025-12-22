from allauth.account.signals import user_signed_up
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver
from requests import get
from django.core.files.base import ContentFile

@receiver(user_signed_up)
def save_google_user_photo(request, user, **kwargs):
    try:
        social_account = SocialAccount.objects.get(user=user, provider='google')
        picture_url = social_account.extra_data.get('picture')
        reponse = get(picture_url)
        if picture_url:
            user.photo.save(
                f"{user.username}_google_photo.jpg",
                ContentFile(reponse.content),
                save=True
            )
            user.save()
    except SocialAccount.DoesNotExist:
        pass

@receiver(user_signed_up)
def save_user_nickname(request,user,**kwargs):
    user.nickname = user.username.replace("_"," ")
    user.save()