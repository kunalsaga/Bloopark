
class student:

    def __init__(self, id, firstName, lastName) -> None:
        self.id= id
        self.firstName = firstName
        self.lastName = lastName


class enrolled:
    def __init__(self, id, year, stdId) -> None:
        self.id =id
        self.year =year
        self.studentId = stdId


def count_john( std_list):
    cnt =0

    for i in std_list :
        if i.firstName == "john":
            cnt+=1

    return cnt     

def data_correction( table):
    for i in table:
        if i.id >20 and i.id<100:
            i.year=2015



if __name__ == "__main__":
    list_of_stud =[ student(1,"john","walker"),student(2,"kunal","saga"),
                    student(3,"john","pote"),student(4,"nita","singh"),
                    student(5,"neha","saga"),student(6,"john","patil"),
                    student(7,"payal","sinha"),student(8,"john","jacob")]

    ans = count_john(list_of_stud)
    print(ans,'\n')


    random_data = [enrolled(30,2002,256),enrolled(1,2000,258),
                enrolled(80,2012,260),enrolled(130,2015,262),
                enrolled(300,1998,263),enrolled(55,2011,264),
                enrolled(420,2006,270),enrolled(122,2009,271),
                enrolled(37,2020,275),enrolled(99,2021,273),]
    
    data_correction(random_data)

    for i in random_data:
        print(i.id," ", i.year)
