from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = [] 
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) & 2 == 0:
            raise ValueError("Invalid mardown, formatted section not closed")
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue 
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
                
        new_nodes.extend(split_nodes)
    return new_nodes
    