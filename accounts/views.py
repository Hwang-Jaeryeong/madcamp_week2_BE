# accounts/views.py
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView

from allauth.socialaccount.models import SocialToken


class NaverLoginView(OAuth2LoginView):
    adapter_class = NaverOAuth2Adapter
    client_class = OAuth2Client

    def get_success_url(self):
        # SocialAccount를 통해 특정 사용자의 네이버 소셜 계정을 가져옵니다.
        social_account = SocialAccount.objects.filter(user=self.request.user, provider='naver').first()

        if social_account:
            try:
                # SocialToken을 통해 액세스 토큰을 가져옵니다.
                social_token = SocialToken.objects.get(account=social_account)

                # 액세스 토큰 출력 또는 활용
                access_token = social_token.token
                print(f"네이버 액세스 토큰: {access_token}")

                # 여기서 액세스 토큰을 사용하여 추가적인 작업을 수행할 수 있습니다.
                # 예를 들어 네이버 API에 요청을 보내서 사용자 정보를 가져오는 등의 작업이 가능합니다.

            except SocialToken.DoesNotExist:
                print("SocialToken이 존재하지 않습니다.")
            except Exception as e:
                print(f"액세스 토큰을 가져오는 중 에러 발생: {e}")

        return super().get_success_url()

