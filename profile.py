import geni.portal as portal
import geni.rspec.pg as rspec


# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()

tourDescription = \
"""
Our goal is to automate the entire process. Once we create the CloudLab profile it will create an environment that automatically downloads and installs docker. We want to reach the expected benchmarks on the paper so we want to update Docker on the CloudLab profile to be able to reach these expectations. This process will be automated as well, so that shortly after Docker is installed it will be updated and configured properly to be able to hit the expected goals of the benchmarks. Then we will run tests on the profile that we are looking into and comparing them to the benchmark to show that the automation was a success.
"""

# Create a XenVM
node = request.XenVM("node")
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
node.routable_control_ip = "true"

node.addService(rspec.Execute(shell="/bin/sh",
                              command="sudo apt update"))
node.addService(rspec.Execute(shell="/bin/sh",
                              command="sudo apt install -y apache2"))
node.addService(rspec.Execute(shell="/bin/sh",
                              command='sudo suwf allow in "Apache Full"'))
node.addService(rspec.Execute(shell="/bin/sh",
                              command='sudo systemctl status apache2'))
# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
