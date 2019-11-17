select class 
from leetcode_0596
group by class
having count(distinct(student))>=5;