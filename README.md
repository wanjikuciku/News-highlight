# News Highlight
A web application that gives various news source and allow users to read articles:https://lony-highlights.herokuapp.com/ by Wanjiku Lorna

## Description
A web application that displays various news sources on the homepage. It gives users an option to view the articles displayed and read the full article as well.


## Set-up and Installation
To start using this project use the following commands:

* git clone https://github.com/wanjikuciku/News-highlight.git
* cd News
* atom .
* code .(this is it visual studio is your preferred text editor). 

To run this program

* Create a virtual environment by python3.6 -m venv --without-pip virtual then activate the virtual environment

* Read the specs and requirements files and install all requirements by pip install -r requirements.txt

* create a start.sh file and hide it in gitignore

* Edit the start.sh file with your email account and password and add python3.6 manage.py server so as to serve

* enter the code chmod a+x start.sh then ./start.sh to serve

* access the application on this localhost address http://127.0.0.1:5000

## Specifications
| Behaviour  | Input   | Output  |
|------------|---------|---------|
| View General Category | general sources | Display all sources in the general category, click to view articles and overflow is hidden|
| View Tech Category | technology sources | Display all sources in the technology category, click to view articles and overflow is hidden |
| View Business Category | business sources | Display all sources in the business category, click to view articles and overflow is hidden |
| View Fun category | fun sources | Display all sources in the fun category, click to view articles and overflow is hidden |
| View Sports Category | sports sources | Display all sources in the sports category, click to view articles and overflow is hidden |

## Live Demo
Here is a link to a live demo : https://lony-highlights.herokuapp.com/

## Known Bugs
None known at the moment.

## Technologies Used
* Python
* HTML
* BOOTSTRAP


## License
MIT License

Copyright (c) 2018 Lorna Wanjiku

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.