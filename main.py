#!/usr/bin/python
""" main

Crawler of Devost project sites from EUvsVirusHackathon for D4G
EUvsVirusCluster project.

Script crawls endpoints provided by devpost-api project by ViRb3
(https://github.com/ViRb3/devpost-api):
(1) docker pull virb3/devpost-api:latest
(2) docker run -p 5000:5000 virb3/devpost-api:latest
(3) Access API at http://127.0.0.1:5000
    - endpoints:
        /user/:username [NA for this project]
        /project/:project_name

Author: datadonk23
Date: 07.05.20 
"""

