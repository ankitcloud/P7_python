from __future__ import print_function
import sys
import libvirt

stgvol_xml = """
<volume>
 <name>again2.img</name>
 <allocation>0</allocation>
 <capacity unit="G">2</capacity>
 <target>
 <format type='qcow2'/>
 <permissions>
 <owner>107</owner>
 <group>107</group>
 <mode>0744</mode>
 <label>virt_image_t</label>
 </permissions>
 </target>
</volume>"""

poolName = 'default'
conn = libvirt.open('qemu:///system')
if conn == None:
 print('Failed to open connection to qemu:///system', file=sys.stderr)
 exit(1)

pool = conn.storagePoolLookupByName(poolName)
if pool == None:
 print('Failed to locate any StoragePool objects.', file=sys.stderr)
 exit(1)

stgvol = pool.createXML(stgvol_xml, 0)
if stgvol == None:
 print('Failed to create a StorageVol objects.', file=sys.stderr)
 exit(1)

exit(0)