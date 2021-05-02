import datetime
class Skills():

    def Experience(self):

        x = datetime.datetime.now()
        cur_year = x.strftime("%Y")
        cur_mon = x.strftime("%m")
        year = int(cur_year) - int(2017)
        month = int(year) * 12
        a = int(cur_mon) - 6
        exp_mon = a + month
        total_exp_y = exp_mon / 12
        total_exp_m = exp_mon % 12
        print("*Total experience of " + str(int(total_exp_y)) + " years and " + str(total_exp_m) + " months in Software testing")
        print('''\
        *Hands On experience in tools of Software Testing. 
        *Worked on real life projects’ scenario in which had great exposure of the flow of project, design, 
        documentation, development as a whole life cycle. 
        *Excellent time management skills with proven ability to work accurately and quickly prioritize coordinate 
        and consolidate tasks. 
        *Good logical and analytical skills. 
        ''')

    def Automation(self):
        print('''\
        Experience in testing Web Applications through Automation.
        Webdriver: Selenium
        Language: Python
        Framework: Robot Framework
        ''')
    def Manual(self):
        print('''\
        Manual testing:
        *Test Plans
        *Test Cases & Processes
        *Regression Testing
        *Test strategies & Coverage
        *UI compatibility Testing
        *Defect and Bugs Discovery
        *Mobile testing
        *Windows Application Testing
        *Hardware integration testing
        *Windows and Server virtual machines setup
        *Upgrade testing
        *Localization testing
        ''')

    def Tools(self):\
        print('''\
        Experience with following Tools:
        *JIRA
        *Mantis
        *HP ALM QC
        *VCommander
        *TFS
        ''')
    def Qualification(self):

        print('''\
        Degree: B. tech in Computer Science - 2017 
        [Punjabi University]: 6.5 (CGPA)
        
        Class XII (PCM) - 2013
        C.B.S.E.: 60%
        
        Class X - 2011
        C.B.S.E.: 7.6(CGPA) 
        ''')

    def Contact(self):
        print('''\
        Ph.: +917009137490, 8968280068
        E-mail: mitulkataria@live.com ''')


    def Organizations(self):
        print('''\
        Organization 1: Seasia Infotech, Mohali
        Client: Becton Dickinson, Chandigarh (Working On - site)
        Date: June 2020 – Present
        Designation: Consultant, Software Quality
        City: Mohali
        
        Organization 2: Technocrats Horizons Compusoft, Mohali
        Date: October 2019 – April 2020
        Designation: Sr. Quality Analyst
        City: Mohali 
        
        Organization 3: Open Access Technologies, Mohali
        Date: June 2017 – September 2019
        Designation: Quality Analyst
        City: Mohali 
        
        Organization 4: Practo Technologies Pvt Ltd. (Internship)
        Date: January 2017 – April 2017
        Designation: Quality Analyst
        City: Bengaluru
        ''')
    def hobbies(self):
        print('''\
        My hobbies are:
        *Team Sports (Football)
        *Photography
        *Cycling
        *Squash
        *Badminton
        ''')
    def all(self):
        obj.Contact()
        obj=Skills()
        obj.Experience()
        obj.Organizations()
        obj.Manual()
        obj.Automation()
        obj.Qualification()
        obj.Tools()
        obj.hobbies()
