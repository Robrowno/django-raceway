from django.shortcuts import render
from profiles.models import UserProfile,CardStorage
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.

def check_user_profile(user):
    return UserProfile.objects.filter(user=user).exists()
# def check_user_card(user):
#     return CardStorage.objects.filter(user=user).exists()
def profile(request):

    """
    A view for the user profile page
    """
    user = request.user
    context={}
    if(check_user_profile(user)):
        print(check_user_profile(user))
        profile = UserProfile.objects.get(user=user)
        context={'profile':profile}
        return render(request, 'profiles/profile.html',context)
    # if(check_user_card(user)):
    #     card = CardStorage.objects.get(user=user)
    #     context={'card':card}

def edit_profile(request):

    """
    A view to edit the user profile
    """

    return render(request, 'profiles/edit-profile.html')
