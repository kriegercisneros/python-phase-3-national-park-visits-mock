# Object Relations Code Challenge - National Park Visits
(Original from https://github.com/emileypalmquist/python-phase-3-practice-challenges)

For this assignment, we'll be working with a national park planner-style domain.

We have three models: `NationalPark`, `Visitor`, and `Trip`.

For our purposes, a `NationalPark` has many `Trip`s, a `Visitor` has many
`Trip`s, and a `Trip` belongs to a `Visitor` and to a `NationalPark`.

`NationalPark` - `Visitor` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has tests to help you check your work. You
can run `pytest` to make sure your code is functional before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

#### Visitor

- `Visitor __init__(self, name)`
  - Visitor should be initialized with a name
- `Visitor property name`
  - Return name
  - Names must be of type `str`
  - Names must be between 1 and 15 characters, inclusive

#### NationalPark

- `NationalPark __init__(self, name)`
  - NationalParks should be initialized with a name, as a string
- `NationalPark property name`
  - Returns the NationalPark's name
  - Should not be able to change after the NationalPark is created
  - hint: hasattr()

#### Trip

- `Trip __init__(self, visitor, national_park, start_date, end_date)`
  - Trips should be initialized with a visitor, national_park, start_date(str), end_date(str)

### Object Relationship Methods and Properties

#### Trip 
Trip is the Join Table between Visitors and National Parks 

- `Trip property Visitor`
  - Returns the visitor object for that trip
  - Must be of type `Visitor`
- `Trip property NationalPark`
  - Returns the NationalPark object for that trip
  - Must be of type `NationalPark`

#### Visitors

- `Visitor trips()`
  - Returns a list of all trips for that visitor
  - The list of trips must contain type `Trip`
- `Visitor nationalparks()`
  - Returns a **unique** list of all parks who that visitor has visited.
  - The list of national parks must contain type `NationalPark` 

#### NationalPark

- `NationalPark trips()`
  - Returns a list of all trips planned for this national park
  - The list of trips must contain type `trip`
- `NationalPark visitors()`
  - Returns a **unique** list of all visitors a national park has recieved
  - The list of visitors must contain type `Visitor`

### Aggregate and Association Methods

#### Visitor

- `Visitors create_trip(national_park, start_date, end_date)`
  - given a **national park object**, a start_date and end_date (as a string), creates a
    new Trip and associates it with that visitor and national park.

#### National Park

- `NationalPark total_visits()`
  - Returns the total number of times that park has been visited
- `NationalPark best_visitor()`
  - Returns the Visitor 
