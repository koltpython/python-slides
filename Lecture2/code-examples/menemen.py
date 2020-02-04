print("Chop the tomatoes")
print("Deseed and slice the peppers")
print("Cook the vegetables until they soften")
print("Crack and cook the eggs")

print("Slice the onions")
print("Chop the tomatoes")
print("Deseed and slice the peppers")
print("Cook the onions until they soften")
print("Cook the vegetables until they soften")
print("Crack and cook the eggs")


def prepare_base_vegetables():
    print("Chop the tomatoes")
    print("Deseed and slice the peppers")

def cook():
    print("Cook the vegetables until they soften")
    print("Crack and cook the eggs")

def menemen_without_onions():
    prepare_base_vegetables()
    cook()

def menemen_with_onions():
    print("Slice the onions")
    prepare_base_vegetables()
    print("Cook the onions until they soften")
    cook()  

prepare_base_vegetables()
cook()

print("Slice the onions")
prepare_base_vegetables()
print("Cook the onions until they soften")
cook()
