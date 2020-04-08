Documentation of scooter-sharing APIs in Atlanta.

UPDATE 4/8/20 - Most scooter companies have left Atlanta.  🤷‍♀️

Previous version:
Atlanta is struggling with how to regulate scooters.
 City ordinance requires the publication of scooter data [via an API](https://library.municode.com/ga/atlanta/codes/code_of_ordinances?nodeId=PTIICOORENOR_CH150TRVE_ARTXSHDOMODE_S150-406DASH
).

That data could help make better regulations — it could answer questions like how many scooters sit unused for how long. And what percent of scooters are placed in which parts of town.

So far, I'm having little luck finding any such API from the city or most scooter operators.

Therefore, right now this repo contains little!

But it has at least two purposes:
1. Document scooter-sharing APIs in Atlanta
2. Show simple examples of how to extract the data using Python

The examples will extract to .csv so that you need not be some pro data scientist to read it.  A pro would already know how to do this. But if you're new to Python, this is meant for you.

**Jump**

API: 

Bike: https://gbfs.uber.com/v1/atlb/free_bike_status.json
Scooter: https://gbfs.uber.com/v1/atls/free_bike_status.json

**Other resources**

A [repo by ubahnverleih and others](https://github.com/ubahnverleih/WoBike) that documents a bunch of bike/scooter-share APIs.
