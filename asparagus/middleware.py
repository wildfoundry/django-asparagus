import objgraph

from django.conf import settings


class TrackObjectLeaks:
    """Prints objects that leak accross a request."""

    def process_request(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        objgraph.show_growth(limit=1)
        return None

    def process_response(self, request, response):
        objgraph.show_growth(limit=100)

        track_class_name = getattr(settings, 'ASPARAGUS_TRACK_CLASS', None)

        if track_class_name:
            objgraph.show_chain(
                objgraph.find_backref_chain(
                    objgraph.by_type(track_class_name)[-1],
                    objgraph.is_proper_module
                ),
                filename='leaks.png'
            )

        return response
