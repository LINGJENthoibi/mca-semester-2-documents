import copy

original_list = [1, 2, [3, 4]]
shallow_copy_list = copy.copy(original_list)
deep_copy_list = copy.deepcopy(original_list)

shallow_copy_list[2][0] = 5
shallow_copy_list[0] = 10

print("original list :", original_list)
print("shallow copied list :", shallow_copy_list)
print("Deep copied list :", deep_copy_list)


