import unittest 
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        html_node = HTMLNode("a", "This is a anchor tag", ["<p>"], {"href": "https://www.google.com"})
        html_node2 = HTMLNode("a", "This is a anchor tag", ["<p>"], {"href": "https://www.google.com"})
        self.assertEqual(html_node, html_node2)
        
    def test_props_to_html(self):
        html_node = HTMLNode("a", "This is a anchor tag", ["<p>"], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            'href="https://www.google.com" target="_blank"', html_node.props_to_html()
        )
        
    def test_eq_false(self):
        html_node = HTMLNode("a", "This is a anchor tag", ["<p>"], {"href": "https://www.google.com"})
        html_node2 = HTMLNode("h1", "This is a h1 tag", ["<div>"], {"href": "https://www.linkedin.com"})
        self.assertNotEqual(html_node, html_node2)
        
if __name__ == "__main__":
    unittest.main()