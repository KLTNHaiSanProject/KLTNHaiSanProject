from sys import path
path.insert(1,path[0]+'\\configs')
import variables
database_target={
    'user':variables.user_target,
    'password':variables.pass_target,
    'host':variables.host_target,
    'port':'5432',
    'database':variables.databasename_target
}

database_source=[
    {
        'user':"ivf_toan",
        'password':'To@n147789',
        'host':'172.16.1.219',
        'port':'5432',
        'database':'medi_2007'
    }
]
