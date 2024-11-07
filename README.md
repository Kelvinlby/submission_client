# submission_client
- This is the source code of a conda package designed for kelvinlby/submission
- It is designed to send data generated during ML training process to submission

# Attention
- Please install grpcio & grpcio-tools from conda-forge channel manually
- If something happens to the "libmamba.so.20" in your conda, refer to this issue ContinuumIO/anaconda-issues/issues/13353

# Installation
- Install grpcio & grpcio-tools
> make sure that you have both grpcio & grpcio-tools 1.67.0 or newer
```shell:
    conda install -c conda-forge grpcio
    conda install -c conda-forge grpcio-tools
```
- Run this command in the terminal
 ```shell
    conda install patrick_echo_hello_world::submission
```

# Usage
- import this module in python
```Python
    from submission import *
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
