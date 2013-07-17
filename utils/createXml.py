'''
Created on 2013-7-16

@author: siwei
'''

import xml.etree.cElementTree as ET

def createXmlTree(user):
    '''
    create an xml file contains contents such as:
    <root>
        <parent1>
            <child1>foo</child1>
        </parent1>
        <parent2>
            <child2>bar</child2>
        </parent2>
    </root>
    children_list must be fetched through parent_list
    
    return the tree unicode string
    '''

    root = ET.Element("root")
    containers = user.container_set.order_by('id')
    for one_container in containers:
        p_tag = ET.SubElement(root, 'category', {"name": one_container.name})
        for one_link in one_container.linker_set.order_by('id'):
            c_tag = ET.SubElement(p_tag, 'a', {"href": one_link.link})
            c_tag.text = one_link.name

    return ET.tostring(root, 'unicode')

        
if __name__ == '__main__':
    pass