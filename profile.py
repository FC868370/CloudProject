import geni.portal as portal
import geni.rspec.pg as pg
import geni.rspec.igext as IG

pc = portal.Context()
request = pc.makeRequestRSpec()

tourDescription = \
"""
Our goal is to automate the entire process. Once we create the CloudLab profile it will create an environment that automatically downloads and installs docker. We want to reach the expected benchmarks on the paper so we want to update Docker on the CloudLab profile to be able to reach these expectations. This process will be automated as well, so that shortly after Docker is installed it will be updated and configured properly to be able to hit the expected goals of the benchmarks. Then we will run tests on the profile that we are looking into and comparing them to the benchmark to show that the automation was a success.
"""

#
# Setup the Tour info with the above description and instructions.
#  
tour = IG.Tour()
tour.Description(IG.Tour.TEXT,tourDescription)
request.addTour(tour)

prefixForIP = "192.168.1."
link = request.LAN("lan")

for i in range(3):
  if i == 0:
    node = request.XenVM("head")
  else:
    node = request.XenVM("worker-" + str(i))
  node.cores = 4
  node.ram = 8192
  node.routable_control_ip = "true" 
  node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
  iface = node.addInterface("if" + str(i))
  iface.component_id = "eth1"
  iface.addAddress(pg.IPv4Address(prefixForIP + str(i + 1), "255.255.255.0"))
  link.addInterface(iface)
  node.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/install_docker.sh"))
  
pc.printRequestRSpec(request)
