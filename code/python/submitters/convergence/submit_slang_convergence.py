from lib.experiments.submitters import submit_python_jobs

# Import your experiment definitions here:
from experiments.convergence_experiments.slang_convergence_final import experiment_name, variants

# Write your call to the job submitter here:
submit_python_jobs(experiment_name, variants, method='SLANG', cv=0)
