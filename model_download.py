from huggingface_hub import snapshot_download
import os

# os.chdir("./models")

ignore_patterns = ["*.ot", "*.h5", "*.onnx", "*.safetensors", "*.msgpack"]
snapshot_download(
    repo_id="huawei-noah/TinyBERT_General_4L_312D",
    ignore_patterns=ignore_patterns,
    cache_dir=r"D:\Sharanya Personal\UCSD\Course content",
)
