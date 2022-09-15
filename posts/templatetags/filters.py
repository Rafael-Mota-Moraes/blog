from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()


@register.filter(name='plural_comentarios')
@stringfilter
def plural_comentarios(num_comentarios):
    try:
        num_comentarios = int(num_comentarios)

        if num_comentarios == 0:
            return f'Nenhum Comentário'
        elif num_comentarios == 1:
            return f'{num_comentarios} Comentario'
        else:
            return f'{num_comentarios} Comentarios(s)'

    except:
        return f'{num_comentarios} Comentario(s)'
