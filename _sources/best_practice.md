# Best Practices

Modeled on the [CryoCloud Best Practices](https://book.cryointhecloud.com/content/hub_best_practices.html)

***

After loggin in and clicking `Launch server`, there are two options to select: `environment` and `resource allocation`. 
* Environment: Select Pangeo Notebook Image to start a python environment with a set of common geoscience packages including those from the [Pangeo](https://pangeo.io/#ecosystem) ecosystem. This is the environment required to run our example notebooks. 
* Resource: Please select the smallest resource (RAM and CPUs) which can meet your needs for a given workflow. The higher resource options cost us signficantly more. You can see your memory usage at the bottom of the screen when working in a notebook.  


***
To avoid unneccessary costs, please shutdown your server when you finish on the Hub:
* `File` > `Hub Control Panel` > `Stop Server`
* Once the `Stop Server' button disappears, your server has stopped
* Click `Log Out`
* Close that browser tab before starting the server again to prevent errors

*** 

The hub will automatically shut off after 90 minutes without activity. 

*** 

Please keep saved files in your home directory to a minimum. Let us know if you need to store more than around 10GB. We recommend workflows which stream data without downloading to a file, or which automatically delete files after using them. You can check total usage by running the following command in a terminal: `du -hs --exclude="shared*" ~/`. 

*** 

Packages can be installed using pip (`% pip install packagename`) if the standard Pangeo environment does not have them. However, these installs only last for the duration of that session.

*** 




