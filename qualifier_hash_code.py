f = open("f_libraries_of_the_world.txt","r")
contents = f.readlines()
line_1 = contents[0].split(" ")
line_2 = contents[1].split(" ")
different_books, number_of_libraries, number_of_days = int(line_1[0]), int(line_1[1]), int(line_1[2])
#print("Number of books , number of libraries , number of days ", different_books, number_of_libraries, number_of_days)
score_of_books = []
for i in range(len(line_2)):
    score_of_books.append(int(line_2[i]))
#print(score_of_books)
number_of_libraries_copy = number_of_libraries
books_per_library, signup_process_for_library, library_ships_books_number, all_books_ids, list_of_all_book_ids_in_order = [], [], [], [], []
i = 2
while number_of_libraries_copy > 0:
    line_library_specifications = contents[i].split(" ")
    line_books_ids = contents[i + 1].split(" ")
    books_per_library.append(int(line_library_specifications[0]))
    signup_process_for_library.append(int(line_library_specifications[1]))
    library_ships_books_number.append(int(line_library_specifications[2]))
    for j in range(len(line_books_ids)):
        all_books_ids.append(int(line_books_ids[j]))
    list_of_all_book_ids_in_order.append(all_books_ids)
    all_books_ids = []
    i += 2
    number_of_libraries_copy -= 1
#print(books_per_library, signup_process_for_library, library_ships_books_number)
#print(list_of_all_book_ids_in_order)
f.close()
output_efficiency = []
for i in range(len(signup_process_for_library)):
    output_efficiency.append((number_of_days - signup_process_for_library[i]) * library_ships_books_number[i])
#print(output_efficiency)

#libraries_chosen_for_signing = []
#for i in range(len(signup_process_for_library)):
#   libraries_chosen_for_signing.append(int(output_efficiency.index(max(output_efficiency))))
#    output_efficiency[(int(output_efficiency.index(max(output_efficiency))))] = -1

#total_time_taken_for_signing = 0
#x = 0
#while total_time_taken_for_signing < number_of_days and x != len(signup_process_for_library):
#    total_time_taken_for_signing = total_time_taken_for_signing + libraries_chosen_for_signing[x]
#    x += 1

#print(libraries_chosen_for_signing)

num = 0
for i in range(len(output_efficiency)):
    if output_efficiency[i] > 0:
        num += 1


f1 = open("output_f.txt", "a")
f1.write(str(num) + "\n")
#print(len(libraries_chosen_for_signing))
x=0
#while len(libraries_chosen_for_signing) > x:
#    f1.write(str(libraries_chosen_for_signing[x]) + " ")
#    print(libraries_chosen_for_signing[x], end=" ")
#    if books_per_library[x] <= number_of_days:
#        f1.write(str(books_per_library[x]) + "\n")
#        print(books_per_library[x])
#    for i in range(len(list_of_all_book_ids_in_order[x])):
#        f1.write(str(list_of_all_book_ids_in_order[x][i]) + " ")
#        print(list_of_all_book_ids_in_order[x][i], end=" ")
#    f1.write("\n")
#    print("")
#    x += 1

while num > x:
    if output_efficiency[x] < 0:
        x += 1
        continue
    f1.write(str(x) + " ")
#    print(x, end=" ")
    f1.write(str(books_per_library[x]) + "\n")
#        print(books_per_library[x])
    for i in range(len(list_of_all_book_ids_in_order[x])):
        f1.write(str(list_of_all_book_ids_in_order[x][i]) + " ")
#        print(list_of_all_book_ids_in_order[x][i], end=" ")
    f1.write("\n")
#    print("")
    x += 1

f.close()