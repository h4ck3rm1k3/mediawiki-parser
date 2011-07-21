from constants import html_entities

def render_tag_p(attributes):
    return '\n'

def render_tag_br(attributes):
    return '\n'

allowed_tags = {'p': render_tag_p,
                'br': render_tag_br}

def render_title2(node):
    node.value += '\n'

def render_title6(node):
    node.value += '\n'

def render_raw_text(node):
    pass

def render_paragraph(node):
    node.value += '\n'

def render_body(node):
    pass

def render_entity(node):
    value = '%s' % node.leaf()
    if value in html_entities:
        node.value = '%s' % unichr(html_entities[value])
    else:
        node.value = '&%s;' % value

def render_lt(node):
    pass

def render_gt(node):
    pass

def process_attributes(node, allowed_tag):
    result = ''
    if len(node.value) == 1:
        pass
    elif len(node.value) == 2:
        attributes = node.value[1].value
        for i in range(len(attributes)):
            attribute_name = attributes[i].value[0].value
            attribute_value = attributes[i].value[1].value
            result += ' %s="%s"' % (attribute_name, attribute_value)
    else:
        raise exception, "Bad AST shape!"
    return result

def render_tag_open(node):
    tag_name = node.value[0].value
    if tag_name in allowed_tags:
        attributes = process_attributes(node, True)
        tag_processor = allowed_tags[tag_name]
        node.value = tag_processor(attributes) 
    else:
        attributes = process_attributes(node, False)
        node.value = '<%s%s>' % (tag_name, attributes)

def render_tag_close(node):
    node.value = ''

def render_tag_autoclose(node):
    tag_name = node.value[0].value
    if tag_name in allowed_tags:
        attributes = process_attributes(node, True)
        tag_processor = allowed_tags[tag_name]
        node.value = tag_processor(attributes) 
    else:
        attributes = process_attributes(node, False)
        node.value = '<%s%s />' % (tag_name, attributes)

toolset = {'render_raw_text': render_raw_text,
           'render_paragraph': render_paragraph,
           'render_title2': render_title2,
           'render_title6': render_title6,
           'render_body': render_body,
           'render_entity': render_entity,
           'render_lt': render_lt,
           'render_gt': render_gt,
           'render_tag_open': render_tag_open,
           'render_tag_close': render_tag_close,
           'render_tag_autoclose': render_tag_autoclose}

from mediawiki_parser import wikitextParser

def make_parser():
    return wikitextParser.make_parser(toolset)
