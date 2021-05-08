global_name = "Josh"

def some_function():
    local_name = "Also Josh"
    global global_name
    global_name = "test"
    #global_name="test"
    print(f"Global is: {global_name}")
    print(f"Local is: {local_name}")

some_function()
print(global_name)

