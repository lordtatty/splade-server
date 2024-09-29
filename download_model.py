import os
from spladerunner import Expander

def download_model():
    # Set the cache directory to ./splade_model
    cache_dir = "./splade_model"

    # Create an instance of Expander to trigger model download
    expander = Expander(model_name="Splade_PP_en_v1", cache_dir=cache_dir)
    print(f"Model downloaded and stored in {os.path.abspath(cache_dir)}")

if __name__ == "__main__":
    download_model()
