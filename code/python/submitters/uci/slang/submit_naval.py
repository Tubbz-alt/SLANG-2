from lib.experiments.submitters import submit_python_jobs

# Naval
from experiments.uci.uci_slang_experiments_bo_naval import experiment_name, variants
submit_python_jobs(experiment_name, variants, method='UCI_SLANG_BO', cv=0)
