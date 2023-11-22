from.schoolapp.table import create_Admintable,create_tutortable,create_studentable



def migration():
    create_Admintable()
    create_tutortable()
    create_studentable()
    print("migration ran")
