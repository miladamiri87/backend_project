def get_client_ip(request):
    _xff = request.META.get('HTTP_X_FORWARDED_FOR')
    if _xff:
        return _xff.split(',')[0]

    return request.META.get('REMOTE_ADDR')
