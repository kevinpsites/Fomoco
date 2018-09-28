from catalog import models as cmod

class LastFiveMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        ids = request.session.get("id_list")
        product_list = []
        if ids is not None:
            for id in ids:
                product_list.append(cmod.Product.objects.get(id=id))

        request.last_five = product_list
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        i_list = []
        for product in request.last_five:
            i_list.append(product.id)
        request.session["id_list"] = i_list

        return response
