import re # imports regex


# global variables:
short_template_dark_and_stormy = "../assets/dark_and_stormy_night_template.txt" # initial test template
long_template_video_game = "../assets/video_game.txt" # actual game template

def welcome_message():
  """
  function prints out welcome message and instructions to user
  """

  print("""
Welcome to Madlibs!

- To quit at any time enter "quit"

- You will be asked to pick a long or short story

- You will then be prompted to enter a series of words such as nouns or verbs. 

- These words will be substituted for blanks in a story. 

- Finally, you get to read the story you helped create!

- Have fun!
""")

def game_start():
  """
  function starts game
  asks user to pick long or short story
  function will select long or short template based on user imput
  if the user enters "quit" the game will close
  """
  print("Would you like to play using a long or short story?")
  individual_user_input = input(">>> ")

  if individual_user_input != "QUIT":

    if individual_user_input.lower() == "short":
      print("Opening short game...")
      play_the_game(short_template_dark_and_stormy)

    if individual_user_input.lower() == "long":
      print("Opening long game...")
      play_the_game(long_template_video_game)

  else:
    print("Goodbye!")

def play_the_game(asset_template_file_chosen_by_user: str):
  """
  function accepts user input string as value
  function creates and appends user input to empty list
  function opens story template chosen by user
  function parses placeholder words from the template and prints them to user,
   promps user to enter a noun, adjective or verb 
  function turns user input into tuple
  function will merge tupled list of user input into the preselected template
  function prints finished template to user
  function invokes save_story_function to save finished story to assets folder
   as "user_input_storage"
  """

  # function set up: reades and parses template
  list_of_user_input = []
  opened_template_file_chosen_by_user = read_template(asset_template_file_chosen_by_user)
  returns_everything_between_curly_brackets_in_templates = parse_template(opened_template_file_chosen_by_user)

  # list of nouns, verbs and adjectives from template
  list_of_nouns_adjectives_verbs_from_template = returns_everything_between_curly_brackets_in_templates[1]
  template_with_curly_bracket_strings_removed = returns_everything_between_curly_brackets_in_templates[0]

  # for loop loops through template selected by user and prints a request for the value in the template (noun, verb, adjective).  If user enters quit, game will be exited.
  for each_adjective_verb_etc_being_asked_for in list_of_nouns_adjectives_verbs_from_template:
    print("Enter a(n):", each_adjective_verb_etc_being_asked_for)
    individual_user_input = input("Enter here >> ")

    if individual_user_input != 'QUIT':
      list_of_user_input.append(individual_user_input)

    else:
      print("Thanks for playing")
      quit()

  tupled_list_of_user_inputs = tuple(list_of_user_input)
  completed_story_output = merge(template_with_curly_bracket_strings_removed, tupled_list_of_user_inputs)

  print(completed_story_output)
  save_story(completed_story_output)

# function saves completed story to assets folder
def save_story(completed_story_saved_to_assets_folder):
  with open("../assets/user_input_storage.txt", "w") as asset_template_file_chosen_by_users:
    asset_template_file_chosen_by_users.write(completed_story_saved_to_assets_folder)

# main function invocations
def main_function_invocations():
  """
  function invokes game
  """

  welcome_message()
  game_start()

# function opens and reads file string
def read_template(str):
  """
  function takes in a string
  function opens a file for reading only
  funciton will return string "File does not exist" if it cannot find the file
  """

  with open(str, "r") as template_file:
    try:
      contents = template_file.read()
      return contents
    except FileNotFoundError as error:
      print(error, "File does not exist!")

# function parses string inside curly brackets from template and returns string without curly brackets. Tuple makes it so it can't be changed. Regex credits to Cassie Bradshaw(code review)
def parse_template(str):
  """
  function parses template to access string between curly brackets
  function turns the string into tuple
  """

  stripped = str

  parts = tuple(re.findall(r"\{(.*?)\}", stripped))

  str = re.sub(r"\{(.*?)\}", "{}", stripped)

  return (str, parts)

# merges string and tuple together
def merge(str, tuple):
  """
  function merges string and tuple
  """

  return str.format(*tuple)

if __name__ == "__main__":
  main_function_invocations()








