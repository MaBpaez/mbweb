"""
Adding a canonical tag in Django
"""


def canonical(request):
    # stuff needed before defining context

    context = {
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
        'CANONICAL': True,
        # any other context variables needed
    }

    return context
