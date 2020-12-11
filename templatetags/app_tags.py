from django import template
import datetime
register=template.Library()

@register.simple_tag(name="get_date") #you can use any value of 'name'
def get_date():
    now=datetime.datetime.now()
    return now
@register.filter
def quotes(value):
    s='"'+str(value)+'"' #you canconvert it to string if it's not a string
    return s
