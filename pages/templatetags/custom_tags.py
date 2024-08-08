from django import template
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def include_template(context, template_name):
    template_paths = {
        'Home title section': 'home/title.html',
        'Home second section': 'home/second_section.html',
        'Home third section': 'home/third_section.html',
        'Home invoice section': 'home/invoice_section.html',
        'Home our blog section': 'home/our_blog_section.html',
        'Home SEO section': 'home/seo_section.html',


    }

    template_path = template_paths.get(template_name)
    if template_path:
        return mark_safe(render_to_string(template_path, context.flatten()))
    return ''
