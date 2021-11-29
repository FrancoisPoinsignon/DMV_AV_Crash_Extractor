# DVA_Data

Python script to extract DVA Autonomous crash infos from PDF reports to a single CSV file.

## How to install
1/ Pull or download the code  
2/ Install poppler https://blog.alivate.com.au/poppler-windows/ (for Windows)  
3/ Add "C:\Program Files\poppler-0.68.0\bin" as a PATH environment variable  


## How to use
1/ Download the crash AV reports from https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/autonomous-vehicle-collision-reports/ and put them in the "reports" folder. (2021 reports are already in)   
2/ Run "main.py" in a console:  
```bash
python main.py
```
3/ The CSV data associated will be stored in a "data<datetime>.csv" file (a CSV file for 2021 is already created)
