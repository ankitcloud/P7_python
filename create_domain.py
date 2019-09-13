# New VM is created with given configuration

from __future__ import print_function
import sys
import libvirt
import time

ts = time.time()
name = 'VM_demo'+str(ts)
memory = '1024'
image = 'slax'
current_cpu = '1'
available_cpu = '4'
disk = '10240'

f = open("xml/volume.xml", "r")
stgvol_xml = f.read()
f.close()
stgvol_xml = stgvol_xml.replace('$name$',name)
stgvol_xml = stgvol_xml.replace('$disk$',disk)

f = open("xml/domain.xml", "r")
xmlconfig = f.read()
f.close()
xmlconfig = xmlconfig.replace('$name$',name)
xmlconfig = xmlconfig.replace('$memory$',memory)
xmlconfig = xmlconfig.replace('$image$',image)
xmlconfig = xmlconfig.replace('$current_cpu$',current_cpu)
xmlconfig = xmlconfig.replace('$available_cpu$',available_cpu)

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

pool = conn.storagePoolLookupByName('default')
if pool == None:
 print('Failed to locate any StoragePool objects.', file=sys.stderr)
 exit(1)

# Volume is created in pool available (configuation in volume.xml)
stgvol = pool.createXML(stgvol_xml, 0)
if stgvol == None:
 print('Failed to create a StorageVol objects.', file=sys.stderr)
 exit(1)

# VM is created (configuation in domain.xml)
dom = conn.defineXML(xmlconfig)
if dom == None:
    print('Failed to define a domain from an XML definition.', file=sys.stderr)
    exit(1)

if dom.create() < 0:
    print('Can not boot guest domain.', file=sys.stderr)
    exit(1)

print('Guest '+dom.name()+' has booted', file=sys.stderr)

conn.close()
exit(0)
