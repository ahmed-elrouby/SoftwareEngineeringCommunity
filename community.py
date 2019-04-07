class Post:
    #Post_ID=0
    Post_Name=""
    Contant=""
    Status=""
    Filed=""
    User_ID=0
    def AddNewPost(self,postname,contant,status,filed,userid):
        self.Post_Name=postname
        self.Contant=contant
        self.User_ID=userid
        self.Status=status
        self.Filed=filed
    def Print(self):
        print(self.User_ID)
        print(self.Post_Name)
        print(self.Contant)
        print(self.Status)
        print(self.Filed)
    def DeletePost(self,postname,userid):
        print("delete")
    def Update(self,postname,userid):
        print("update")
    def SharePost(self,postname,userid):
        print("show")

class Vacancy:
    #VacancyID=0
    VacancyName=""
    Title=""
    Requirement=""
    Type=""
    CompanyID=0
    def AddNewVacancy(self,vacancyid,vacancyname,title,requirement,type,companyid):
        self.VacancyID=vacancyid
        self.VacancyName=vacancyname
        self.Title=title
        self.Requirement=requirement
        self.Type=type
        self.CompanyID=companyid
        if (self.CompanyID>=0):
            print("companyid")
    def Print(self):
        print(self.VacancyID)
        print(self.VacancyName)
        print(self.Title)
        print(self.Requirement)
        print(self.Type)
        print(self.CompanyID)
    def DeleteVacancy(self,vacancyname,companyid):
        print("delete")
    def UpdateVacancy(self,vacancyname,companyid):
        print("update")
    def ShareVacancy(self,vacancyname,companyid):
        print("show")


class Follow:
    UserID=0
    FollowerID=0
    FollowsID=0
    def MakeFollow(self,userid):
        print("follow")
v=Vacancy()
v.Print()
