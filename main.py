def main():
  path = "./books/frankenstein.txt"
  text = read_file(path)
  word_count = get_num_words_from_text(text)
  character_count_dict = get_character_count_in_text(text)
  print_report(character_count_dict, path, word_count)

def read_file(path):
  with open(path) as f:
    text = f.read()
  return text

def get_num_words_from_text(text):
    words = text.split(" ")
    return len(words)

def get_character_count_in_text(text):
  text = text.lower()
  import re
  filtered_text = re.sub("[^a-z]","",text)
  character_count = {}
  for character in filtered_text:
    if character in character_count:
      character_count[character] += 1
    else:
      character_count[character] = 1
  return character_count

def print_report(char_dict, path, word_count):
  print(f"--- Begin report of {path} ---")
  print(f"{word_count} words found in the document")

  list_of_character_count = chars_dict_to_sorted_list(char_dict)
  for obj in list_of_character_count:
    print(f"The '{obj["letter"]}' character was found {obj["count"]} times")
  print("--- End report ---")

def sort_on(dict):
  return dict["count"]

def chars_dict_to_sorted_list(char_dict):
  list = []
  for character, count in char_dict.items():
    list.append({ "letter": character, "count": count })
  list.sort(reverse=True, key=sort_on)
  return list


main()