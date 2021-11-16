#!/usr/env python
# eXtensible Markup Language
'''
XML also like HTML uses 'tags' <>
ex:
<people>
    <person> # Complex element
        <name>Alex</name> # Simple element
        <phone>5555555</phone> # Simple element
    <person>

XML basics
<person>    # start tag
    <name>Alex</name>  # end tag
    <phone type="intl">  # attribute
    555 555 5555
    </phone> # end tag
    <email hide="yes" /> # attribute + self closing tag
</person> # end tag
In XML vs HTML we get to make up our tags vs using anchors and etc. you still most follow the </name> closing rule
Tabs and whitespace doesn't actually matter in XML unless it is txt like the phone number


XML attributes use the syntax key="string" there is not href="string" like in HTML
XML Terminology 
Tags - Include the beginning and ending of elements 
Attributes - Keyword/value pairs on the opening tag of XML
Serialize/De-Serialize - Convert data in one program into a common format that can be stored and/or
transmitted between systems in a programming language-independent manner

XML Text and Attributes
XML tags can have many attributes assigned to them in a Kay/Value pair but they only use one TXT section
EX:
<a>
    <b w="5">X</b>
<a>

XML Schema - Describing a 'contract' as to what is acceptable in XML
'''