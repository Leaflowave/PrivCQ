adult

***adult_info: 
three attributes: 
age: [17, 90] to [1，9] 保留十位，不round 9 possible values
education: [1, 16] 16 possible values
hourperweek [1, 99] to [0-9] 保留十位，不round 10 possible values
lists of lists, containing all information


***adult_group:
{hourspw: [[]]}
group owners in terms of hourspw, 只含数据库中已有的hourspw，而不是domain内所有可能的值

***adult1:
{age: count}

***adult2:
{(age, education): count}

***adult3:
{(age, education, hourspw): count}