from django.shortcuts import render
from profiles.models import UserProfile, CardStorage
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def check_user_profile(user):
    """
    Checks to see if user profile already exists
    """
    return UserProfile.objects.filter(user=user).exists()


def check_user_card(user):
    """
    Checks to see if user card already exists
    """
    return CardStorage.objects.filter(user=user).exists()


@login_required
def profile(request):
    """
    A view for the user profile page
    """
    user = request.user
    if (check_user_profile(user)):
        profile = UserProfile.objects.get(user=user)
        context = {'profile': profile, 'user': user}
    return render(request, 'profiles/profile.html', context=context)


@login_required
def update_profile(request):
    """
    For updating profile information
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        address1 = request.POST.get('Address1')
        address2 = request.POST.get('Address2')
        city = request.POST.get('city')
        county = request.POST.get('County')
        nationality = request.POST.get('Nationality')
        postal_code = request.POST.get('PostalCode')
        user = request.user
    try:
        UserProfile.objects.filter(user=user).update(
            default_phone_number=tel,
            default_street_address1=address1,
            default_street_address2=address2,
            default_town_or_city=city,
            default_county=county,
            default_nationality=nationality,
            default_postcode=postal_code
        )
        message = "Information saved successfully! \n"
        userEmailFlag = True
        userNameFlag = True

        if email != user.email:
            if User.objects.filter(email=email).exists():
                userEmailFlag = False
                message = 'Please enter a different email. This is already in use.\n'
        if userEmailFlag and email != user.email:
            User.objects.filter(id=user.id).update(
                email=email,
            )
        if name != user.username:
            if User.objects.filter(username=name).exists():
                userNameFlag = False
                message = 'Please enter a different username. This is already in use.\n'
        if userNameFlag and name != user.username:
            User.objects.filter(id=user.id).update(
                username=name,
                email=email,
            )
        return JsonResponse({"status": message})
    except Exception as e:
        return JsonResponse(
            {"status": "We got an error. Please try again later."})
