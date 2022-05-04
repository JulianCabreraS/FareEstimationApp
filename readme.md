# Fare Estimation App

### File Structure
- Classes: this folder contains two clases: 
  - Point: This class defines a point (latitude and longitud) at a time (timestamp)
  - Trip: This class defines a trip as a tripid with a set of Points
- File: this folder hosts the files that need to be read (paths.csv) and the file that the system writes  (output.csv)
- Utils - Contains functions libraries that can be reused by classes and function as wells. 
  - Constant: contains fare amounts for each of the conditions 
  - Distance: contains the function that calculate the distance between 2 points. 
  - File Management: General methods for file management read/write 


