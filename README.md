DataCity: A Validation Platform for Data
========================================

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
[![DOI](https://zenodo.org/badge/256060429.svg)](https://zenodo.org/badge/latestdoi/256060429)


Welcome to Data City! Data City is an investigation/validation platform for different datasets pertaining between the
people and the government. Our motivation serves as a possible way to validate data "as it comes in" rather than after the
dataset is collected then published leading to messy data and mismatched records. 

DataCity was built for the CapsuleHack 2020 and below is our first implementation of DataCity and the methods involved. 
 
 
DISCLAIMER: ANY OF THE 
 
 With the rise of open source reporting platforms like  `Open Data Network`, `Spot Crime`, `Community Map` it's
become easier for regular citizens to file police reports without having to go through the arduous police system. Folk
can also report crime in real time. 


System Architecture
===================

DataCity will need to have three components in order to make it a viable platform for continous analytics. 

- **1st Component**: A method of fetching the data and a large scalable platform to do so. DataCity will have an in-house 
                     concourse CI system that will have URLs to scrape from and collect/parse data. This system will be built
                     on digital ocean where the master node is the concourse web service that will serve as our interface
                     for running jobs for daily collection. The concourse CI will fetch data from three platforms: Community Map,
                     SpotCrime, and Dallas OpenData. Each request will be run on a 24 hour cycle when the Dallas Police Crime
                     Department updates their website with the appropiate Daily Crime Report.  

DataCity will have three components that will make it a viable platform for all users that want to enter as a citizen.

- A Concourse System that will run a continuous real time acquisition of other city data and bring them into data city.
- A potential python mid layer that will serve as an API.
- A web application that you can browse and check out data as you wish. 


Announcements
=============

- June 19th 2020 Intiailizing of the Repository.

Open Source Data Standards
==========================

**Crime**: DataCity provides a common data model for encapsulating information

Genesis
=======

DataCity was designed for capsulehack.io and is the dream for three young developers who want to follow their path in centralizing all data. 

- Full Stack Developer [Suliman sharif](http://sulstice.github.io/)

* * * * *

External links
==============

- Houston Police Department Crime Statistics (https://www.houstontx.gov/police/cs/beatpages/beat_stats.htm)
- Austin Police Department Crime Statistics (https://data.austintexas.gov/Public-Safety/Crime-Reports/fdj4-gpfu/data)
- Dallas Police Department Crime Statistics (https://dallaspolice.net/resources/Pages/Crime-reports.aspx) 


