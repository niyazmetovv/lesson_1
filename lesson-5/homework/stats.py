def enrollment_stats(university):
    all_students = [university[1] for university in universities]
    all_fees = [university[2] for university in universities]
    return all_students, all_fees

def mean(my_list):
    return sum(my_list) / len(my_list)

def median(my_list):
    my_list.sort()
    length = len(my_list)
    if length % 2 == 0:
        return (my_list[length // 2] + my_list[(length // 2) - 1])/2
    else:
        return my_list[length // 2]

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
student, tuition = enrollment_stats(universities)
print(f"Total students: {sum(student):,}")
print(f"Total tuition: ${sum(tuition):,} \n")
print(f"Student mean: {mean(student):,.2f}")
print(f"Student median: {median(student):,} \n")
print(f"Tuition mean: {mean(tuition):,.2f}")
print(f"Tuition median: {median(tuition):,}")

