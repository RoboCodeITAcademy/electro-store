from .models import Category, Product

def view_all(request):
    context = {
        "categories":Category.objects.all()
    }
    return context