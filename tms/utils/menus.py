from django.urls import resolve

from menu import MenuItem


class ViewMenuItem(MenuItem):
    """Custom MenuItem that checks permissions based on the view associated
    with a URL"""

    def check(self, request):
        """Check permissions based on our view"""
        is_visible = True
        match = resolve(self.url)

        # do something with match, and possibly change is_visible...

        self.visible = is_visible
