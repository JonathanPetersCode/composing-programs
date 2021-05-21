def parent(name, other_name):
    def child_name(name):
        print(f"My name is {name} I have a sister")

    def child_name_two(other_name):
        print (f"My name is {name} and I have a brother")

    if len(name) > 3:
        return "Name is long enough"
    else:
        return "Ok fine"


print(parent("jack", "mary"))
