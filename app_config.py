import os

# Application (client) ID of app registration
CLIENT_ID = '308a7f3c-843f-4d30-96d1-9dcc89c1f21c'
# Application's generated client secret: never check this into source control!
CLIENT_SECRET = 'Yso8Q~WOvd7VkbQFYFoPiZGC08SJY8n7tPaEXbsu'

# AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
AUTHORITY = f"https://login.microsoftonline.com/58dc8138-f686-4508-96ef-0d3fa7c7ab06"

REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
# The absolute URL must match the redirect URI you set
# in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All"]

# Tells the Flask-session extension to store sessions in the filesystem
SESSION_TYPE = "filesystem"
# Using the file system will not work in most production systems,
# it's better to use a database-backed session store instead.
