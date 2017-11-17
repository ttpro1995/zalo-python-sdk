class APIException(Exception):
    def __init__(self, message, code=None, method=''):
        if code == 400:
            error_400 = "Error 400 HTTP method %s is not supported by this URL" % method
            super(APIException, self).__init__(error_400)
        elif code == 404:
            super(APIException, self).__init__("Error 404 Not Found")
        else:
            super(APIException, self).__init__(message)
