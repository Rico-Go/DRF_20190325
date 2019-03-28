from django.template import Library
from markdown import markdown

regster = Library()

# markdown
@regster.filter
def md(value):
    return markdown(value)