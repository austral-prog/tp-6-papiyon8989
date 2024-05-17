def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 6:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif len(list_to_remove_elements) == 5:
        del list_to_remove_elements[5]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif 0 < len(list_to_remove_elements) < 5:
        del list_to_remove_elements[0]
        return list_to_remove_elements    
    else:
        return(list_to_remove_elements)

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, "Pink")
    list_to_add_elements.insert(6, "Yellow")
    return list_to_add_elements


def is_empty(list_to_check):
    if not list_to_check:
        return True
    else:
        return False

def check_lists(list_to_compare1, list_to_compare2):

    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False
    else:
        return False

def list_of_lists(list_of_lists_to_modify):
    lista1 = list_of_lists_to_modify [0]
    lista2 = list_of_lists_to_modify [1]
    lista3 = list_of_lists_to_modify [2]

    if len(lista1) >= 2 and lista2 >= 4 and lista3 >= 2:
        lista1_0 = lista1 [1]
        lista1_1 = lista1 [0] 
        lista1_2 = [lista1_0, lista1_1]

        lista2_0 = lista2 [3]
        lista2_1 = lista2 [1]
        lista2_2 = [lista2_0, lista2_1]

        lista3_0 = lista3 [-1]
        lista3_1 = lista3 [-2]
        lista3_2 = [lista3_0, lista3_1]

        new_list = [lista1_2, lista2_2, lista3_2]
        return = new_list

    elif 0 < len(lista1) < 2 and len(lista2) >= 4 and len(lista3) >= 2:

        lista1_1 = lista1 [0] 
        lista1_2 = [lista1_1]

        lista2_0 = lista2 [3]
        lista2_1 = lista2 [1]
        lista2_2 = [lista2_0, lista2_1]

        lista3_0 = lista3 [-1]
        lista3_1 = lista3 [-2]
        lista3_2 = [lista3_0, lista3_1]

        new_list = [lista1_2, lista2_2, lista3_2]
        return = new_list

    elif len(lista1) == 0 and len(lista2) >= 4 and len(lista3) >= 2:

        lista2_0 = lista2 [3]
        lista2_1 = lista2 [1]
        lista2_2 = [lista2_0, lista2_1]

        lista3_0 = lista3 [-1]
        lista3_1 = lista3 [-2]
        lista3_2 = [lista3_0, lista3_1]

        new_list = [lista2_2, lista3_2]
        return = new_list

    elif len(lista1) >= 2 and len(lista2) < 4 and len(lista3) >= 2:
        lista1_0 = lista1 [1]
        lista1_1 = lista1 [0] 
        lista1_2 = [lista1_0, lista1_1]

        lista2_1 = lista2 [1]
        lista2_2 = [lista2_1]

        lista3_0 = lista3 [-1]
        lista3_1 = lista3 [-2]
        lista3_2 = [lista3_0, lista3_1]

        new_list = [lista1_2, lista2_2, lista3_2]
        return = new_list

        elif len(lista1) >= 2 and len(lista2) < 2 and len(lista3) >= 2:
        lista1_0 = lista1 [1]
        lista1_1 = lista1 [0] 
        lista1_2 = [lista1_0, lista1_1]

        lista3_0 = lista3 [-1]
        lista3_1 = lista3 [-2]
        lista3_2 = [lista3_0, lista3_1]

        new_list = [lista2_2, lista3_2]
        return = new_list
def list_of_lists(list_of_lists_to_modify):
    return "ANSWER HERE"  # Remove this line and implement
