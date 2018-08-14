import scores, csv
if __name__ == '__main__':
  with open('problems.csv') as probfile:
    with open('users.csv',) as usefile:
      problemsReader = csv.reader(probfile)
      problems = list(problemsReader)
      names = csv.reader(usefile)
      print(scores.score_dict(names, problems))