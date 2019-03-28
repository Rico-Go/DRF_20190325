from django.template import Library
from markdown import markdown

regster = Library()

@regster.filter
def md(value):
    return markdown(value)