import hydra
from omegaconf import DictConfig, OmegaConf

from ImageProcessingManager import ImageProcessingManager


@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(cfg : DictConfig) -> None:
    print(f"CONFIGURATION\n{OmegaConf.to_yaml(cfg)}")

    
    if cfg.paths.image_path_to_analyse:
        img_processor = ImageProcessingManager(cfg.paths.log_images_path)
        img_processor.analyse(
            images_path=cfg.paths.image_path_to_analyse,
            **cfg.analysis
        )
    if cfg.paths.depths_path_to_analyse:
        img_processor = ImageProcessingManager(cfg.paths.log_depths_path)
        img_processor.analyse(
            images_path=cfg.paths.depths_path_to_analyse,
            **cfg.analysis
        )



if __name__ == "__main__":
    my_app()