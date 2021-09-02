# Automation tests for www.orbitz.com website.

## Setup

* Clone the repo `git clone https://github.com/andreykutsenko/OrbitzTests.git`
* Create and activate Python virtual environment
```
cd OrbitzTests
python3.9 -m venv env
. ./env/bin/activate
```
* Update pip `pip install -U pip`
* Install dependencies `pip install -r requirements.txt`


## Running tests

* Run a feature file by using -i or --include flags and then the name of the feature file.

    `behave -i search.feature`

    or `behave --include search`

    or `behave`

* Also you can run a scenario by using -t tag `behave -t '@smoke_kts'`


## Allure, test report generation

Allure integrates with behave as an external formatter.

* Installation `pip install allure-behave`
* Usage:

    You can specify the formatter directly in the command line:

    $ behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features

    Example `behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/search.feature`

    To show allure results: allure serve <results_folder>

    Example `allure serve test_results/`

## Additional 
### Install python 3.9

Install wget using brew `brew install wget`

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

### Drivers

Selenium requires a driver to interface with the chosen browser. 
Firefox, for example, requires `geckodriver <https://github.com/mozilla/geckodriver/releases>`_, which needs to be installed before the below examples can be run.
Make sure it's in your `PATH`, e. g., place it in `/usr/bin` or `/usr/local/bin`.

Failure to observe this step will give you an error `selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.`

Other supported browsers will have their own drivers available. Links to some of the more popular browser drivers follow.
 
| **Chrome**:  | https://sites.google.com/a/chromium.org/chromedriver/downloads        |

| **Firefox**: | https://github.com/mozilla/geckodriver/releases                       |
