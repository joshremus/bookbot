
def main():

    cc = {}

    file_path = "books/frankenstein.txt"

    with open(file_path) as f:
        file_contents = f.read()

    f.close
    
    #print(file_contents)

    wc = word_count(file_contents)

    # print(f"Word Count: {wc}")

    cc = char_count(file_contents)

    # sorting values in descending order
    
    #print(f"Character Count: {cc}")
    print(f"--- Begin report of {file_path} ---")
    print(f"{wc} words found in the document\n")
    
    # print(cc)
    for citem in cc:
        #print(cc[citem])
        
        print(f"The '{citem}' character was found {cc[citem]} times")

    print("--- End report ---")

def word_count(contents):

    words = contents.split()

    return len(words)

def char_count(c_contents):

    d_list = {}

    list_of_c = list(c_contents)
    for lower_item in list_of_c:
        lower_item = str(lower_item.lower())
        
        if lower_item in d_list:
            d_list[lower_item] = d_list[lower_item] + 1
        else:
            d_list[lower_item] = 1

        if lower_item.isalpha() == False:
            del d_list[lower_item]
        #if lower_item.isalpha() == True:
            # print("yip")
            #print(f"yip: {lower_item}")
        #else:
        #    del d_list[lower_item]


    d_list_sorted = dict(sorted(d_list.items(), key=lambda item: item[1], reverse=True))   
    # print(d_list_sorted)
    return d_list_sorted


main()
