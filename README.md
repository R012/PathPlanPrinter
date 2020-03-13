# PathPlanPrinter

Just a simple tool to print planned paths onto a map represented as an image.

## Python version
This code has been tested on Python 3.7. Whilst compatibility with other versions of Python might be possible, it is by no means assured.
Any issues arising as a result of using the wrong version of Python are, therefore, the user's responsibility.

## Dependencies
* PIL, alternatively, Pillow

## Usage
1. Copy `src/PathPlanPrinter.py` into your dependencies or `lib` directory, and import it as you normally would.
2. Create an instance of the PathPlanPrinter class to use. You must pass a list of tuples representing your path plan and a string referencing the source image's location as argument. Additionally, you may also pass a specific path for the output image's location. Should you decide not to, this path will be generated automatically, under the same folder the input resides.
3. If the program properly instances the class, call the `print_plan` method in the newly created object.
	* If the program raises any exceptions, make sure to read them thoroughly before filing a bug report.
