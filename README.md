# vaccine-notifier-wa
Notify the user for the availability of the Vaccine as per the https://prepmod.doh.wa.gov/. 
This repo uses Github actions to run a scheduled job every 30 mins and fail the test if appointments found for the searched parameters.

All you need to do is fork the repo, and change the parameters in notify.py and that's it. GHA will automatically notify as a failure whenever there's any appointments available. 

Stay safe, get vaccinated! 
