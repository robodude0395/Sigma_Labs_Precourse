authorised_names = ["alice", "bob"]

name = input("Hello! What's your name? ")

if name.lower() in authorised_names:
  print(f"Hello {name.title()}!")
else:
  print("Sorry... You are not authorised to be greeted!")