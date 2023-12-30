from django.shortcuts import render,redirect
from .models import Calculation
from .forms import Calculationform
from decimal import Decimal, ROUND_DOWN

# Create your views here.

# def home(request):
#     form = Calculationform()

#     if request.method == "POST":
#         # Create a mutable copy of the QueryDict
#         mutable_post = request.POST.copy()

#         form = Calculationform(mutable_post)
#         if form.is_valid():
#             a = form.cleaned_data['var1']
#             b = form.cleaned_data['var2']

#             # Perform calculation
#             result = a * b

#             # Update the form's data directly
#             mutable_post['var3'] = result

#             # Create a new form with the updated data
#             form = Calculationform(mutable_post)
    
#     return render(request, 'home.html', {'form': form})

# def home(request):
#     form = Calculationform()
#     result = None

#     if request.method == "POST":
#         # Create a mutable copy of the QueryDict
#         mutable_post = request.POST.copy()

#         # Extract the selected operation from the form data
#         operation = mutable_post.get('operation')

#         # Create a form instance with the submitted data
#         form = Calculationform(mutable_post)

#         if form.is_valid():
#             # Retrieve values from the form
#             var1 = form.cleaned_data['var1']
#             var2 = form.cleaned_data['var2']

#             # Perform calculation based on the selected operation
#             if operation == 'add':
#                 result = var1 + var2
#             elif operation == 'subtract':
#                 result = var1 - var2
#             elif operation == 'multiply':
#                 result = var1 * var2
#             elif  operation == 'divide':
#                 if var2 != 0:
#                     result = var1 / var2
#                 else:
#                     result = None
#             else:
#                 result = None

#             # Update the mutable form data with the calculated result
#             mutable_post['var3'] = result

#             # Create a new form instance with the updated data
#             form = Calculationform(mutable_post)

#             # Save the form data to the model instance (if needed)
#             calculation_instance = form.save()

#     return render(request, 'home.html', {'form': form})

def home(request):
    form = Calculationform()
    result = None

    if request.method == "POST":
        # Create a mutable copy of the QueryDict
        mutable_post = request.POST.copy()

        # Extract the selected operation from the form data
        operation = mutable_post.get('operation')

        # Create a form instance with the submitted data
        form = Calculationform(mutable_post)

        if form.is_valid():
            # Retrieve values from the form
            var1 = form.cleaned_data['var1']
            var2 = form.cleaned_data['var2']

            # Perform calculation based on the selected operation
            if operation == 'add':
                result = var1 + var2
            elif operation == 'subtract':
                result = var1 - var2
            elif operation == 'multiply':
                result = var1 * var2
            elif operation == 'divide':
                if var2 != 0:
                    result = var1 / var2
                    result = result.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                else:
                    result = None
            else:
                result = None

            # Update the mutable form data with the calculated result
            mutable_post['var3'] = result

            # Create a new form instance with the updated data
            form = Calculationform(mutable_post)

            if result is not None:
                try:
                    # Save the form data to the model instance only if result is not None
                    calculation_instance = form.save()
                except Exception as e:
                    print(f"Error saving calculation instance: {e}")
                    # Print the form errors for debugging
                    print(form.errors)

    return render(request, 'home.html', {'form': form})