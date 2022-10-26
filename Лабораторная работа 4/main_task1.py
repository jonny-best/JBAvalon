def get_count_char(str_):
      # TODO посчитать количество каждой буквы в строке в аргументе str_
      count_dict = {}
      for i in str_.lower():
          if i.isalpha() and i not in count_dict:
              count_dict[i] = 1
          elif i.isalpha():
              count_dict[i] += 1
      return count_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

