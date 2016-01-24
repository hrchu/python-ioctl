
def check_fd(fd):
    """ Validate that a fd parameter looks like a file descriptor.

    Raises an exception if the parameter is invalid.

    :param fd: File descriptor to check.
    """

    if not isinstance(fd, int):
        raise TypeError('fd must be an integer, but was {}'.format(fd.__class__.__name__))
    if fd < 0:
        raise ValueError('fd cannot be negative')

def check_request(request):
    """ Validate a ioctl request parameter.

    Raises an exception if the parameter is invalid.

    :param request: Ioctl request to check.
    """

    if not isinstance(request, int) and not isinstance(request, long):
        raise TypeError('request must be an integer, but was {}'.format(request.__class__.__name__))
    if request < 0:
        raise ValueError('request cannot be negative')
