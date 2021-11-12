#!/usr/env python 
'''
XML Schema- Describing a contract as to what is acceptable XML
Description of the legal format of an XML document
Expressed in terms of constraints on the structure and content of documents
Often used to specify a 'contract' between systems 
"My system will only accept XML that conforms to this particular schema"
If a particular piece of XML meets the specification of the Schema- it is said to 'validate'

XML Document
<person>
    <lastname>Floyd</lastname>
    <age>100</age>
    <dateborn>1900-09-30</dateborn>
</person>

XML Schema
<xs:complexType name="person">
    <xs:sequence>
        <xs:element name="lastname" type="xs:string"/>
        <xs:element name="age: type=xs:integer"/>
        <xs:element name="dateborn" type="xs:date"/>
        </xs:sequence>
</xs:complexType>

# The XML must match the contract exactly

<xs:element name="person">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="full_name"> type="xs:string"
        minOccurs="1'  maxOccurs="10" />
      <xs:element name="child_name" type="xs:string"
        minOccurs="0" maxOccurs="10" />
    </xs:sequence>
  </xs:complexType>
</xs:element>

# XSD Data Types
xs:string
xs:data  yyyy-mm-dd
xs:dateTime  yyyy-mm-ddTHH:MM:SSZ Z= Time Zone which is GMT/UTC by default
xs:decimal 99.99
xs:integer 100
xs:positiveInteger > 0

'''