from django.urls import reverse
# from utils.menus import ViewMenuItem
from menu import Menu, MenuItem

Menu.add_item("dashboard", MenuItem("Dashboard",
                                    reverse("dashboard")))

Menu.add_item("dashboard", MenuItem("Device Management",
                                    reverse("devices:device_overview")))

Menu.add_item("dashboard", MenuItem("My Work",
                                    reverse("my_work")))

Menu.add_item("main", MenuItem("Overview",
                               reverse("project_overview")))

Menu.add_item("main", MenuItem("Releases",
                               reverse("create_project")))

Menu.add_item("main", MenuItem("Test Run & Results",
                               reverse("create_project")))

Menu.add_item("main", MenuItem("Test Cases",
                               reverse("create_project")))

Menu.add_item("main", MenuItem("Reports",
                               reverse("create_project")))

Menu.add_item("login", MenuItem("Signup",
                                reverse("create_project")))

Menu.add_item("login", MenuItem("Reports",
                                reverse("create_project")))

# Menu.add_item("main", MenuItem("Staff Only",
#                                reverse("create_project"),
#                                check=lambda request: request.user.is_staff))
#
# Menu.add_item("main", MenuItem("Superuser Only",
#                                reverse("create_project"),
#                                check=lambda request: request.user.is_superuser))

# Since we use ViewMenuItem here we do not need to define checks, instead
# the check logic will change their visibility based on the permissions
# attached to the views we reverse here.
# reports_children = (
#      ViewMenuItem("Staff Only", reverse("create_project")),
#      ViewMenuItem("Superuser Only", reverse("create_project"))
# )
#
# Menu.add_item("main", MenuItem("Reports Index",
#                                reverse("create_project"),
#                                children=reports_children))
