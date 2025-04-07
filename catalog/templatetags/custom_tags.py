from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    request = context['request']
    params = request.GET.copy()
    for key, value in kwargs.items():
        params[key] = value
    return params.urlencode()