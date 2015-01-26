from django import template

register = template.Library()
@register.assignment_tag
def make_variable(value):
    return value

@register.assignment_tag(takes_context=True)
def start_page(context,value):
    page=context["page_obj"].number
    startpage=int((page/value)-.0001)*value+1
    return startpage

@register.assignment_tag
def end_page(startpage,maxtoshow):
    return startpage+maxtoshow-1