import re
# Welcome message and explanation
print("Welcome to Madlib! Please enter the following prompts correctly for a fun story")


#read madlib template file and parse into usable parts (string)
def read_template():
   with open('template.txt', 'r')as file:
      template = file.read() # template as a string

non_curly = False
story_dict = ''
story_list = []
empty_filler = ''
whole_word_list = []
ignore = ['{','}']
new_list = []


#parse template into usable parts
for char in template:
   if char == '}':
      whole_word_list.append(empty_filler)
      empty_filler = ''
      non_curly = False

   if char == '{':
      non_curly = True #when changing values use single =
      story_list.append(story_dict)
      story_dict = ''

   if non_curly == False:
      if char not in ignore:
         story_dict += char


   else:
      if char not in ignore:
         empty_filler += char



    
#print (story_list, whole_word_list)

for i in whole_word_list:
   user_input = input(f'Enter any word that is a(n): {i}')
   temp = new_list.append(user_input)
  #  if char is in {}
  #     take contents and stringify


print (new_list)


pattern = r"\{([^}]*)\}"
result = re.sub(pattern, lambda x: new_list.pop(0), template)
# prompt the user to submit  series of words to fit the components of the template

#take user input and populate template 
with open('finished_madlib.txt', 'w') as file:
   template = file.write(result)

print(result)

if __name__ == "__main__":
   pass
