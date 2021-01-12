from django.contrib.auth.forms import UserCreationForm

# 서버에 보내도 서버에 반영되지않는다.
class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True