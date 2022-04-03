report_template = """\
We have made {all} observations from tossing a coin: {tails} of them were tails and {heads} of
them were heads. The probabilities are {tails_percent:0.2f}% and {heads_percent:0.2f}%, respectively. Our
forecast is that in the next {n} observations we will have: {next_tails} tail and {next_heads} heads."""

number_of_observations = 3

report_filename = 'report'

report_file_extension = 'txt'