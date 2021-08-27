# OrbitzTests Project

Using Selenium WebDriver with Python + Behave, for implement the following:
- Visit www.orbitz.com website.
- Select Flights
- Select “Roundtrip”.
- Enter “Leaving from” : San Francisco and “Going to”: New York.
- Select “Departing” date to be 2 weeks from today and “Returning” date to be 3 weeks
from today.
- Click on Search.
- Assert that the search results are rendered correctly (Ex: Departure/Arrival location and
dates match the input data).
- Select “Nonstop” flights.
- Select the most expensive flight from the list.
- Click on “Select” and then click on “Select this fare” to book.
- Assert the flight details & price on the flight review page.


## Install python 3.9

Install wget using brew

```
brew install wget
mkdir ~/code
```

Build from source python 3.9, install with prefix to ~/.python folder:

```
wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
tar xvf Python-3.9.*
cd Python-3.9.6
mkdir ~/.python
./configure --enable-optimizations --prefix=/User/USERFOLDER/.python
make -j8
sudo make altinstall
```

Now python3.9 in `/User/USERFOLDER/.python/bin/python3.9`. Update pip:

```
sudo /User/USERFOLDER/.python/bin/python3.9 -m pip install -U pip
```

Ok, now we can pull our project from Git repository, create and activate Python virtual environment:

```
cd code
git pull https://github.com/andreykutsenko/OrbitzTests.git
cd OrbitzTests
python3.9 -m venv env
. ./env/bin/activate
```

How to install Python packages with pip and requirements.txt:

```
pip install -r requirements.txt
```

You can run a feature file by using -i or --include flags and then the name of the feature file.

```
behave -i search.feature
```
or:
```
behave --include search
```
Also you can run a scenario by using -t tag
```
behave -t '@smoke_kts'
```
