def element_len():
    loop_status = None
    while loop_status != "pass":
        try :
            len_mem = int(input("Input number of element in array (1-100) :"))
        except :
            print("Error input")
        if (len_mem>0) and len_mem<=100:
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
    if set(lst) != len(lst):
        reval =  max(set(lst), key = lst.count)
    else : 
        reval = -1
    print(f"Majority element of array is : {reval}")
if __name__ == "__main__":
    majority(element_mem(element_len()))