from .forms import Newsletter

def modal_form(request):
    return {'newsletter': Newsletter(request.POST or None)}