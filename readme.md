# Installation 

* Create a new environment with `python=3.11`: `conda create -n qwen python=3.11`

* Install Pytorch built for `CUDA 12.1`.

* Install custom requirements.

```
cd custom
pip install -r requirements.txt
```

* Soft-link `models` to the directory with Qwen models


**Note**: `csrc/layer_norm` does not seem to speed up inference. It may even slow it down.