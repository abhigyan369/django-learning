from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    # check karo ki user request send kar rha hai kya (POST) ya only visit kar rha hai (GET)
    if request.method == "POST":
        # 1. Bind the submitted data to the form instance
        form = FeedbackForm(request.POST)
        # 2. Check if the data is valid
        if form.is_valid():
            # 3. Access the "cleaned" data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # ... process other fields like subject and message ...
            
            # 4. Send the user to a success page
            return render(request, 'success.html', {'name': name})
    else:
        # If it's a GET request, provide a blank form
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})