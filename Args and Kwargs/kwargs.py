def create_user(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)


create_user("colin", "a", "b", 1, surname="bob", age=27)
