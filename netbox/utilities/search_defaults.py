

def get_search_type_preference(request):
    """
    Obtain the user's preference for types to search, returning
    [''] if none set.
    """
    try:
        if request.user.is_authenticated:
            return request.user.config.get('search.default_types', [''])
    except ValueError:
        pass
    return ['']

def set_search_type_preference(request, search_types):
    """
    Store the last object types in the user preferences
    """
    if request.user.is_authenticated:
        request.user.config.set('search.default_types', search_types, commit=True)
