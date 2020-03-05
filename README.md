# CloudProject

Team Members:  
  Francis Convery,
  Colin Lesser,
  Colin Pigeon, and
  Brandon Fonticoba
  
We are doing the Performance Evaluation Project. Our task is to select four benchmarks from the paper "An Updated Performance Comparison of Virual Machines and Linux Containers" and try to implement them on different hardware on CloudLab. Our goal is to be able to automatically install KVM, Docker, or Singularity on a single CloudLab profile. Able to automate the installation and configuration of our selected benchmarks and run them. Lastly, to be able to automate the entire process within a single CloudLab profile and instantiate/collect at least 20 runs.

Our goal is to automate the entire process. Once we create the CloudLab profile it will create an environment that automatically downloads and installs docker. We want to reach the expected benchmarks on the paper so we want to update Docker on the CloudLab profile to be able to reach these expectations. This process will be automated as well, so that shortly after Docker is installed it will be updated and configured properly to be able to hit the expected goals of the benchmarks. Then we will run tests on the profile that we are looking into and comparing them to the benchmark to show that the automation was a success.
