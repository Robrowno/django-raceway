from django.shortcuts import render

# Create your views here.


def profile(request):

    """
    A view for the user profile page
    """

    return render(request, 'profiles/profile.html')


def edit_profile(request):

    """
    A view to edit the user profile
    """

    return render(request, 'profiles/edit-profile.html')
