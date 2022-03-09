#Task 1: Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, 
#non-scalar verilerden de oluşabilir.

#desired_output_1 = [1,'a','cat',2,3,'dog',4,5]

def flat(f_list):
    if type(f_list) is list:
        for i in f_list:
            yield from flat(i)
    else:
        yield f_list

def flatten(f_list):
    return list(flat(f_list))

input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat_list= flatten(input_list)
print(flat_list)

        
#Task 2: Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.

input_list_2 = [[1, 2], [3, 4], [5, 6, 7]]
#desired output: [[[7, 6, 5], [4, 3], [2, 1]]
desired_output_2 = []

for element in input_list_2:
    if type(element) == list:
        desired_output_2.append(list(reversed(element)))
        
desired_output = list(reversed(desired_output_2))
print(desired_output)
