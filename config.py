import os

f = os.popen('mv -f /bootflash/autoconfig/adriani/running.latest /home/admin/nxos-workshops/running')
who = f.read()
f.close
print "Result:", who
f = os.popen('cd /home/admin/nxos-workshops; git add running')
who = f.read()
f.close
print "Result:", who
f = os.popen('cd /home/admin/nxos-workshops; git commit -m "Latest change"')
who = f.read()
f.close
print "Result:", who
f = os.popen('cd /home/admin/nxos-workshops; chvrf management git push')
who = f.read()
f.close
print "Result:", who
