# Forms 
There are two main ways to build these:
forms.Form: A "manual" form where you define every field from scratch.  
forms.ModelForm: An "automatic" form that looks at one of your existing database models (like Book) 
and builds the form fields for you.  

##  why ??
In Django, while you can write raw HTML <input> tags, we use the forms framework for a few powerful reasons:
Automatic HTML Generation: Django can render the form fields for you using shortcuts like {{ form.as_p }}.
Validation: It automatically checks if the data matches the type (e.g., is this a real email address?).
Security: It includes built-in protection against CSRF (Cross-Site Request Forgery) attacks.  
Clean Data: It converts text input into Python objects (like a datetime object or an integer) via the cleaned_data dictionary.  