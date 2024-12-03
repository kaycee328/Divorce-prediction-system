from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.linkedin_oauth2.views import LinkedInOAuth2Adapter


class LinkedInLogin(SocialLoginView):
    adapter_class = LinkedInOAuth2Adapter
