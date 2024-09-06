import unittest 
from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        html_node = HTMLNode("a", "This is an anchor tag", ["<p>"], {"href": "https://www.google.com"})
        html_node2 = HTMLNode("a", "This is an anchor tag", ["<p>"], {"href": "https://www.google.com"})
        self.assertEqual(html_node, html_node2)
        
    def test_props_to_html(self):
        html_node = HTMLNode("a", "This is an anchor tag", ["<p>"], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            'href="https://www.google.com" target="_blank"', html_node.props_to_html()
        )
        
    def test_eq_false(self):
        html_node = HTMLNode("a", "This is an anchor tag", ["<p>"], {"href": "https://www.google.com"})
        html_node2 = HTMLNode("h1", "This is a h1 tag", ["<div>"], {"href": "https://www.linkedin.com"})
        self.assertNotEqual(html_node, html_node2)
        
class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        leaf_node = LeafNode("a", "This is an anchor tag", {"href": "https://www.google.com"})
        leaf_node2 = LeafNode("a", "This is an anchor tag", {"href": "https://www.google.com"})
        self.assertEqual(leaf_node, leaf_node2)
        
    def test_eq_false(self):
        leaf_node = LeafNode("a", "This is an anchor tag", {"href": "https://www.google.com"})
        leaf_node2 = LeafNode("p", "This is an paragraph tag")
        self.assertNotEqual(leaf_node, leaf_node2)
        
    def test_to_html(self):
        leaf_node = LeafNode("a", "This is an anchor tag", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            '<a href="https://www.google.com" target="_blank">This is an anchor tag</a>', leaf_node.to_html()
        )
        
    
    
        
if __name__ == "__main__":
    unittest.main()