movie

***movie_info: 
three attributes: 
Age [1-7]	We modified this!!!
Gender [1-2] male and female
Rating [1, 5]

!!! we change 1 to 1, 18 to 2,  25 to 3,  35 to 4, 45 to 5, 50 to 6, 56 to 7

***movie_group:
{Rating: [[]]}
group owners in terms of rating, 只含数据库中已有的，而不是domain内所有可能的值

***movie1:
{age: count}

***movie2:
{(age, gender): count}

***movie3:
{(age, gender, rating): count}
