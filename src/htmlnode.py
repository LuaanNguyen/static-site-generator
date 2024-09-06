class HTMLNode: 
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props 
        
    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return (
                self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props
            )
        return False
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props:
            return " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return ""
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

#A LeafNode is a type of HTMLNode that represents a single HTML tag with no children
class LeafNode(HTMLNode):
    def __init__(self, tag, value = None, props = None):
        super().__init__(tag = tag, value = value, children = None, props = props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        elif self.tag == None:
            return self.value
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        
    
#The new ParentNode class will handle the nesting of HTML nodes inside of one another. 
#Any HTML node that's not "leaf" node (i.e. it has children) is a "parent" node.

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props):
        super().__init__(tag = tag, children = children, props = props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("All parent node must have a HTML tag")
        elif self.children == None:
            raise ValueError("All parent node should have a child")
        else:
            children_tags = ""
            for child in self.children:
                children_tags += child.to_html()
            return f"<{self.tag} {self.props_to_html()}>{children_tags}</{self.tag}>"
                
                
    
    
        