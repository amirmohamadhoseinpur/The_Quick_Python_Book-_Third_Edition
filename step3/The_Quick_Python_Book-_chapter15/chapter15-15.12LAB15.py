'''In this lab, you create classes to represent an HTML
document. To keep things simple, assume that each element can contain only
text and one subelement. So the <html> element contains only a <body> ele-
ment, and the <body> element contains (optional) text and a <p> element
that contains only text.
The key feature to implement is the __str__() method, which in turn calls
its subelement's __str__() method, so that the entire document is returned
when the str() function is called on an <html> element. You can assume
that any text comes before the subelement.
Here’s example output from using the classes:
para = p(text="this is some body text")
doc_body = body(text="This is the body", subelement=para)
doc = html(subelement=doc_body)
print(doc)
<html>
<body>
This is the body
<p>
this is some body text
</p>
</body>
</html>'''

class p:
    def __init__(self, text):
        self.text = text

class body:
    def __init__(self, subelement,  text=''):
        self.text = text
        self.subelement = subelement
class html:
    def __init__(self, subelement):
        self.subelement = subelement
    def __str__(self):
        return f'''<html>
<body>
{self.subelement.text}
<p>
{self.subelement.subelement.text}
</p>
</body>
</html>'''

para = p(text="this is some body text")
doc_body = body(text="This is the body", subelement=para)
doc = html(subelement=doc_body)
print(doc)