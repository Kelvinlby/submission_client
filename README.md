# submission_client
- This is the source code of a conda package designed for kelvinlby/submission
- It is designed to send data generated during ML training process to submission
- This is a NIGHTLY release, so don't install it in your base envs
# Attention
- Some users may encounter "NoModuleNamedSubmission" error
- If a dependency error is raised, check this issue: https://github.com/conda/conda/issues/13043
- Don't install this version of package in your base environment

# Installation
- Create a conda environment to test this nightly release
```shell:
    conda create -n test_env
    conda activate test_env
```
- Run this command in the terminal
 ```shell
    conda install patrick_echo_hello_world::submission
```

# Usage
- import this module in python
```Python
    from submission import start_job, log_job, log_metric, end_job
```
- To start a job in submission, use
```Python
    start_job(NAME)
```
- To log your job in submission, use
```Python
    log_job(NAME, VALUE)
```
- To log a metric in submission, use
```Python
    log_metric(NAME, VALUE)
```
- To end a job in submission, use
```Python
    end_job(NAME)
```


