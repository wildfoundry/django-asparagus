Django Asparagus
----------------

This is a Django middleware to track down object leaks in your Django application.

To use it, add ``asparagus.middleware.TrackObjectLeaks`` to ``MIDDLEWARE_CLASSES``. It should be in the first position.

    MIDDLEWARE_CLASSES = ['asparagus.middleware.TrackObjectLeaks'] + MIDDLEWARE_CLASSES

The middleware will print a summary of any objects created but not garbage collected.

if you set the settings ``ASPARAGUS_TRACK_CLASS`` to a name of an object (e.g. ``Thread``, then the middleware will render a PNG of the references to any newly created objects.

Note, this is not something you ever want in production. Best to use it to find leaks then remove it from settings entirely.
