# submission_client
- This is the source code of a conda package designed for kelvinlby/submission
- It is designed to send data generated during ML training process to submission
- This is a NIGHTLY release, so don't install it in your base envs
# Installation
- Download the .tar file
- Move it to YOURPATH/miniconda/conda-bld
- Create a conda environment to test this nightly release
```shell:
    conda create -n test_env
    conda activate test_env
```
- Run this command to install submission
 ```shell
    conda install --use-local submission
```
# Usage
- import this module in python
```Python
    import asyncio
    from submission import start_job, log_job, log_metric, end_job
```
- To start a job in submission, use
```Python
    asyncio.run(submission.start_job(NAME))
```
- To log your job in submission, use
```Python
    asyncio.run(submission.log_job(NAME, VALUE))
```
- To log a metric in submission, use
```Python
    asyncio.run(submission.log_metric(NAME, VALUE))
```
- To end a job in submission, use
```Python
    asyncio.run(submission.end_job(NAME))
```

