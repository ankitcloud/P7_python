from __future__ import print_function
import sys
import libvirt
from xml.dom import minidom
domName = 'VM_demo1568284974.997433'
conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)
dom = conn.lookupByName(domName)
if dom == None:
    print('Failed to find the domain '+domName, file=sys.stderr)
    exit(1)
raw_xml = dom.XMLDesc(0)
xml = minidom.parseString(raw_xml)
f = open("info.xml", "w")
f.write(raw_xml)
conn.close()
exit(0)
