import scores, csv
if __name__ == '__main__':
  with open('problems.csv') as probfile:
    with open('users.csv') as usefile:
      problems = csv.reader(probfile)
      names = csv.reader(usefile)
      print(scores.score_dict(names, problems))