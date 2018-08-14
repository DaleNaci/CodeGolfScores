import scores, csv
if __name__ == '__main__':
  with open('problems.csv') as probfile:
    with open('users.csv',) as usefile:
      problemsReader = csv.reader(probfile)
      problems = list(problemsReader)
      namesReader = csv.reader(usefile)
      names = list(namesReader)
      print(scores.score_dict(names, problems))