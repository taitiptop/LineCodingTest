"""Majority element of an array is defined as a value x for 
   which strictly more than half of array elements are equal to x.
   Output the majority element of the given array a, or -1 if the array doesn't have majority element.
   The first line of the input contains an integer N - the number of elements in the array. 1 <= N <= 100.
   The second line of the input contains N integers - the elements of the array, separated with single spaces. 
    1 <= ai <= 100."""

def element_len():
    loop_status = None
    while loop_status != "pass":
        try :
            len_mem = int(input("Input number of element in array (1-100) :"))
        except :
            print("Error input")
        if (len_mem>0 & len_mem<=100):
            loop_status = "pass"
            return len_mem
        else :
            print("Error input")

def element_mem(len_mem):
    loop_status = None
    while loop_status != "pass":
        try :
            lst_input = input(f"Input {len_mem} elements(1-100) in array separated by single space :").split()
            lst_mem = [int(i) for i in lst_input]
            if len(lst_mem) == len_mem:
                loop_status = "pass"
                return lst_mem
            else :
                print(f"Error input")
        except :
            print("Error input")

def majority(lst):
    if len(set(lst)) != len(lst):
        val_max =  max(set(lst), key = lst.count)
        if lst.count(val_max) > len(lst)/2:
            reval = val_max
        else :
            reval = -1
    else : 
        reval = -1
    print(f"Majority element of array is : {reval}")

if __name__ == "__main__":
    majority(element_mem(element_len()))
