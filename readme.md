# Fare Estimation App

## Use Instructions
1. Load a paths.csv file in [/Files](./files)
2. Run application with the command python appFareEstimation.py
3. Output file will be generated in [/files/output.csv](./files/output.csv)

## Process
**File Reading**
- The application read the CSV file and create a dictionary for each trip. 
- Each point is added to the trip according to the idTrip

**Fare Calculation**
- Each Trip can calculate the fare at any time using recalculateFare method at any time. 

**General Fare Calculation**
- The application iterates over the dictionary and calculate the fare for each trip 

## File Structure
- [Classes](./classes): this folder contains two clases: 
  - Point: This class defines a point (latitude and longitud) at a time (timestamp)
  - Trip: This class defines a trip as a tripid with a set of Points
- [Files](./files): this folder hosts the files that need to be read (paths.csv) and the file that the system writes  (output.csv)
- [Test](./test): This folder contains Test Classes for Utils, Fare Estimation
- [Utils](./utils) - Contains functions libraries that can be reused by classes and function as wells.
  - Constant: contains fare amounts for each of the conditions 
  - Distance: contains the function that calculate the distance between 2 points. 
  - File Management: General methods for file management read/write 


