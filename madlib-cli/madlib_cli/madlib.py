# It was a {Adjective} and {Adjective} {Noun}.

def welcome_message():
  print("""
Welcome to Madlibs!

- You will be prompted to enter a series of words such as nouns or verbs. 

- These words will be substituted for blanks in a story. 

- Finally, you get to read the story you helped create!
""")

welcome_message()

def read_template():
  adjective_prompt = input("Enter an adjective! ")
  adjective_prompt_two = input("Enter an adjective! ")
  noun_prompt = input("Enter a noun! ")
  print("It was a " + adjective_prompt + "and " + adjective_prompt_two + " " + noun_prompt + ".")

  read_template()