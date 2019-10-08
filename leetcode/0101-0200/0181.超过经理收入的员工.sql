select l1.Name as Employee
from leetcode_0181 l1, leetcode_0181 l2
where l1.ManagerId = l2.Id and l1.Salary>l2.Salary ;
