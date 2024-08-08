from django import template
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def include_template(context, template_name):
    template_paths = {
        'News Section': 'home/title.html',
    }

    template_path = template_paths.get(template_name)
    if template_path:
        return mark_safe(render_to_string(template_path, context.flatten()))
    return ''
