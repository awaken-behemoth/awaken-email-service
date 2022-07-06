
import werkzeug


class CustomError(werkzeug.exceptions.HTTPException):
    """Custom error is an abstract created to listen to all errors that are
    not native python errors.
    This allows to use a single @app.errorhandler to listen to all errors without
    interfiering with native error handling performed by flask. Thanks to that, we
    avoid useless boilerplate while not creating silent unhandled error.

    Args:
        werkzeug (_type_): _description_
    """
    pass
