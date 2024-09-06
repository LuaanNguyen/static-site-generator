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
        
    