from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.linkedin_oauth2.views import LinkedInOAuth2Adapter


# class LinkedInLogin(SocialLoginView):
#     adapter_class = LinkedInOAuth2Adapter


class LinkedInLogin(SocialLoginView):
    adapter_class = LinkedInOAuth2Adapter

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        access_token = response.data.get("access_token")
        linkedin_data = get_linkedin_user_info(access_token)
        # Process and save LinkedIn data as needed
        return response
