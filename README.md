**Names:** Alicia Fritz & Jens Hansen

**Purpose:** Our code for Lazy-LinkingIn creates a research foundation for analyzing data from LinkedIn. LinkedIn is a common and powerful tool for creating and expanding professional work connections but it lacks capabilities in analyzing content and cueing users to take actions to improve their networks. This code will enable users to focus on and target members of their network that are particularly valuable based on the criteria provided.

**Reporting bugs or feature requests:** In order to do either of these things for our code, please go to the "Issues" tab in our GitHub repository, click "New Issue," and provide a descriptive title, detailed description, and steps to reproduce (if applicable). Then, submit your issue. We appreciate your feedback and contributions!

**Contributions:** If you would like to contribute to this project, please make your changes in a forked repository, ensuring they meet our coding standards. Then, submit a pull request to our main repository with a descriptive title and detailed description of your changes.

**Installation instructions:** Lazy-LinkingIn is developed in Python and requires the following packages to operate properly: Pandas, NetworkX, Matplotlib, and NumPy. Within the terminal, the python packages must be installed. These dependencies are easily installed within the code through commands to import and install the libraries (e.g. “import pandas”). In the terminal the python package can be installed initially through standard commands (e.g. “pip install python”) Running this code requires a user to have downloaded their LinkedIn data to a .csv file (directions for doing that are in the User Documentation section below). Once that data file has been downloaded the user will need to reference that file name and location within the code. Anytime code references a csv with the phrase “connect” in it, the user will insert their specific file name and address. No additional external tools, programs, or APIs are necessary for this code.
User 

**Documentation:**  In order to use this code a csv file of LinkedIn data is necessary. Accessing this data can be found at [this link]( https://www.linkedin.com/help/linkedin/answer/a1339364/downloading-your-account-data).
The code features are:
  1. The first feature is to analyze connections spatially to understand their degree of similarity with each other and degree of connection and proximity with each other
  2. The second feature analyzes the growth of the network over time and highlights dated connections that might be worth reconnecting with.
  3. The third feature is to analyze the search queries made within the LinkedIn profile to gain insight into the most frequent searches and how often searches are being made.

For the code to run optimally, the .csv file format should have five columns of data with the first four columns containing text data (first name, last name, company, position) and the fifth column having calendar dates (month/day/year). Features one, two, and three will render visualizations with feature one and three also providing some information about the data as an output.
